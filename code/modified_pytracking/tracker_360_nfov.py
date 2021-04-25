import importlib
import os
import sys
import numpy as np
from collections import OrderedDict
from pytracking.evaluation.environment import env_settings
import time
import cv2 as cv
from pytracking.utils.visdom import Visdom
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from pytracking.utils.plotting import draw_figure, overlay_mask
from pytracking.utils.convert_vot_anno_to_rect import convert_vot_anno_to_rect
from ltr.data.bounding_box_utils import masks_to_bboxes
from pytracking.evaluation.multi_object_wrapper import MultiObjectWrapper
from pathlib import Path
import torch

# custom modules to improve equirectangular tracking
from pytracking.evaluation.boundingbox import BoundingBox
from pytracking.evaluation.parser import Parser
from pytracking.evaluation.nfov import NFOV



class Tracker360NFOV:
    """Wraps the tracker for evaluation and running purposes.
    args:
        name: Name of tracking method.
        parameter_name: Name of parameter file.
        video_path: Path of video.
        groundtruth_path: Path of file with annotated objects (groundtruth).
        save_result_path: Path to new file with results.
    """

    def __init__(self, name: str, parameter_name: str, video_path: str, groundtruth_path: str = None, save_result_path: str = None, run_id = None):
        assert run_id is None or isinstance(run_id, int)

        self.name = name
        self.parameter_name = parameter_name
        self.video_path = video_path
        self.groundtruth_path = groundtruth_path
        if save_result_path:
            self.save_result_path = save_result_path
        else:    
            self.save_result_path = "tmp-result-" + self.name.upper() + ".txt"

        self.run_id = None
        
        self.video = None
        self.video_width = None
        self.video_height = None
        self.frame = None
        self.tracker = None
        self.bbox = None
        self.gt_bounding_boxes = []
        self.result_bounding_boxes = []

        # enable parsing/creating methods 
        self.parser = Parser()

        # constants for sizes and positions of opencv circles, rectangles and texts
        self.RECTANGLE_BORDER_PX = 3
        self.FONT_SCALE = 0.75
        self.FONT_WEIGHT = 1
        self.TEXT_ROW1_POS = (30,30)
        self.TEXT_ROW2_POS = (30,60)
        self.TEXT_ROW3_POS = (30,90)
        self.TEXT_ROW4_POS = (30,120)

        self.WINDOW_NAME = "Tracker-" + self.name.upper()
        self.WINDOW_NAME_RECTILINEAR = "Tracker-" + self.name.upper() + "-frame_rectilinear"

        env = env_settings()
        if self.run_id is None:
            self.results_dir = '{}/{}/{}'.format(env.results_path, self.name, self.parameter_name)
        else:
            self.results_dir = '{}/{}/{}_{:03d}'.format(env.results_path, self.name, self.parameter_name, self.run_id)

        tracker_module_abspath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tracker', self.name))
        if os.path.isdir(tracker_module_abspath):
            tracker_module = importlib.import_module('pytracking.tracker.{}'.format(self.name))
            self.tracker_class = tracker_module.get_tracker_class()
        else:
            self.tracker_class = None

        self.visdom = None


    def create_tracker(self, params):
        tracker = self.tracker_class(params)
        tracker.visdom = self.visdom
        return tracker


    def _init_visdom(self, visdom_info, debug):
        visdom_info = {} if visdom_info is None else visdom_info
        self.pause_mode = False
        self.step = False
        if debug > 0 and visdom_info.get('use_visdom', True):
            try:
                self.visdom = Visdom(debug, {'handler': self._visdom_ui_handler, 'win_id': 'Tracking'},
                                     visdom_info=visdom_info)

                # Show help
                help_text = 'You can pause/unpause the tracker by pressing ''space'' with the ''Tracking'' window ' \
                            'selected. During paused mode, you can track for one frame by pressing the right arrow key.' \
                            'To enable/disable plotting of a data block, tick/untick the corresponding entry in ' \
                            'block list.'
                self.visdom.register(help_text, 'text', 1, 'Help')
            except:
                time.sleep(0.5)
                print('!!! WARNING: Visdom could not start, so using matplotlib visualization instead !!!\n'
                      '!!! Start Visdom in a separate terminal window by typing \'visdom\' !!!')


    def _visdom_ui_handler(self, data):
        if data['event_type'] == 'KeyPress':
            if data['key'] == ' ':
                self.pause_mode = not self.pause_mode

            elif data['key'] == 'ArrowRight' and self.pause_mode:
                self.step = True


    def get_parameters(self):
        """Get parameters."""
        param_module = importlib.import_module('pytracking.parameter.{}.{}'.format(self.name, self.parameter_name))
        params = param_module.parameters()
        return params


    # method for drawing rectangle according to points 
    def _drawBoundingBox(self, videoWidth, point1, point2, boundingBox, color, thickness):
        if (boundingBox.is_on_border()):
            # draw two rectangles around the region of interest
            rightBorderPoint = (videoWidth - 1, point2[1])
            cv.rectangle(self.frame, point1, rightBorderPoint, color, thickness)

            leftBorderPoint = (0, point1[1])
            cv.rectangle(self.frame, leftBorderPoint, point2, color, thickness)
        else:
            # draw a rectangle around the region of interest
            cv.rectangle(self.frame, point1, point2, color, thickness)


    # method for saving result bounding boxes to txt file
    def _saveResults(self):
        # creating string result data
        resultData = self.parser.createAnnotations(self.result_bounding_boxes)
        # saving file on drive
        self.parser.saveDataToFile(self.save_result_path, resultData)
        print("File '" + self.save_result_path + "' has been successfully created with total " + str(len(self.result_bounding_boxes)) + " computed frames.")



    # method for start tracking with improvement of mapping equirectangular to rectilinear projection
    def run_video_nfov(self, optional_box=None, debug=None, visdom_info=None):
        params = self.get_parameters()

        debug_ = debug
        if debug is None:
            debug_ = getattr(params, 'debug', 0)
        params.debug = debug_

        params.tracker_name = self.name
        params.param_name = self.parameter_name
        self._init_visdom(visdom_info, debug_)

        multiobj_mode = getattr(params, 'multiobj_mode', getattr(self.tracker_class, 'multiobj_mode', 'default'))

        if multiobj_mode == 'default':
            self.tracker = self.create_tracker(params)
            if hasattr(self.tracker, 'initialize_features'):
                self.tracker.initialize_features()
        elif multiobj_mode == 'parallel':
            self.tracker = MultiObjectWrapper(self.tracker_class, params, self.visdom, fast_load=True)
        else:
            raise ValueError('Unknown multi object mode {}'.format(multiobj_mode))

        ###########################################################################
        #############         Part of custom modifications            #############
        ###########################################################################
        ########## 1) Video Checking ##########
        # Read video
        self.video = cv.VideoCapture(self.video_path)
        # Exit if video not opened.
        if not self.video.isOpened():
            print("Could not open video")
            print(help)
            sys.exit(-1)

        # Read first frame.
        ok, self.frame = self.video.read()
        if not ok:
            print("Error - Could not read a video file")
            sys.exit(-1)

        # save video width/height to global variables
        self.video_width = int(self.video.get(cv.CAP_PROP_FRAME_WIDTH))
        self.video_height = int(self.video.get(cv.CAP_PROP_FRAME_HEIGHT))

        # correct format of initialization bbox
        def _build_init_info(box):
            return {'init_bbox': OrderedDict({1: box}), 'init_object_ids': [1, ], 'object_ids': [1, ], 'sequence_object_ids': [1, ]}


        ########## 2) Setup opencv window ##########
        # resize window (lets define max width is 1600px)
        if self.video_width < 1600:
            cv.namedWindow(self.WINDOW_NAME)
        else:
            cv.namedWindow(self.WINDOW_NAME, cv.WINDOW_NORMAL | cv.WINDOW_KEEPRATIO)
            whRatio = self.video_width / self.video_height
            if whRatio == 2:
                # pure equirectangular 2:1
                cv.resizeWindow(self.WINDOW_NAME, 1600, 800)
            else:
                # default 16:9
                cv.resizeWindow(self.WINDOW_NAME, 1600, 900)

            scaleFactor = self.video_width / 1600
            self.RECTANGLE_BORDER_PX = int(self.RECTANGLE_BORDER_PX * scaleFactor)
            self.FONT_SCALE = self.FONT_SCALE * scaleFactor
            self.FONT_WEIGHT = int(self.FONT_WEIGHT * scaleFactor) + 1
            self.TEXT_ROW1_POS = (int(self.TEXT_ROW1_POS[0] * scaleFactor), int(self.TEXT_ROW1_POS[1] * scaleFactor))
            self.TEXT_ROW2_POS = (int(self.TEXT_ROW2_POS[0] * scaleFactor), int(self.TEXT_ROW2_POS[1] * scaleFactor))
            self.TEXT_ROW3_POS = (int(self.TEXT_ROW3_POS[0] * scaleFactor), int(self.TEXT_ROW3_POS[1] * scaleFactor))
            self.TEXT_ROW4_POS = (int(self.TEXT_ROW4_POS[0] * scaleFactor), int(self.TEXT_ROW4_POS[1] * scaleFactor))

        # use copy of frame to be shown in window
        frame_disp = self.frame.copy()

        ########## 3) Initialation of bounding box ##########
        # Set up initial bounding box
        self.bbox = None
        self.result_bounding_boxes = []
        self.gt_bounding_boxes = []
        if self.groundtruth_path:
            # use first bounding box from given groundtruth
            self.gt_bounding_boxes = self.parser.parseGivenDataFile(self.groundtruth_path, self.video_width)

            if len(self.gt_bounding_boxes) > 0:
                bb1 = self.gt_bounding_boxes[0]
                if bb1.is_annotated:
                    self.bbox = (bb1.get_point1_x(), bb1.get_point1_y(), bb1.get_width(), bb1.get_height())
                    self.result_bounding_boxes.append(bb1)
                else:
                    print("Error - Invalid first frame annotation from file: '" + self.groundtruth_path + "'")
                    sys.exit(-1)
        else:
            # using opencv select ROI
            cv.putText(frame_disp, 'Select target ROI and press ENTER', self.TEXT_ROW1_POS, cv.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 200, 250), self.FONT_WEIGHT)

            x, y, w, h = cv.selectROI(self.WINDOW_NAME, frame_disp, fromCenter=False)
            self.bbox = [x, y, w, h]

            # save it to result list
            p1 = (int(self.bbox[0]), int(self.bbox[1]))
            p2 = (int(self.bbox[0] + self.bbox[2]), int(self.bbox[1] + self.bbox[3]))
            # new instance of bounding box
            bb1 = BoundingBox(p1, p2, self.video_width)
            bb1.is_annotated = True
            self.result_bounding_boxes.append(bb1)

        if not(self.bbox) or self.bbox == (0,0,0,0):
            print("Error - Invalid first frame annotation")
            sys.exit(-1)


        ########## 4) Tracking process ##########
        # prints just basic guide and info
        print("--------------------------------------------------------------------")
        print("pytracking tracking process with rectilinear improvement has started...")
        print("Tracker  : " + self.name.upper())
        print("Frame #1 : " + str(self.bbox))
        print("Press 'Esc' or 'Q' key to exit")
        print("--------------------------------------------------------------------")


        ##########################################################################
        ################## Normal field of view initialization ###################
        ##########################################################################
        # init instance for normal field of view according to rectilinear framework
        nfov_width = int(self.video_width / 2)
        nfov_height = int(self.video_height / 2)

        # lets define max rectilinear window size - 720p
        if nfov_width > 1440 or nfov_height > 720:
            whRatio = nfov_width / nfov_height
            nfov_height = 720
            nfov_width = round(whRatio * 720)

        # create instance of NFOV
        nfov = NFOV(nfov_height, nfov_width)

        # center point of selected bounding box
        center_equi_x = int(self.bbox[0] + self.bbox[2]/2)
        center_equi_y = int(self.bbox[1] + self.bbox[3]/2)
        center_equi_x_normalized = center_equi_x / self.video_width
        center_equi_y_normalized = center_equi_y / self.video_height
        
        # bounding box points left_top and bottom_right
        x1_normalized = self.bbox[0] / self.video_width
        y1_normalized = self.bbox[1] / self.video_height
        x2_normalized = (self.bbox[0] + self.bbox[2]) / self.video_width
        y2_normalized = (self.bbox[1] + self.bbox[3]) / self.video_height

        # camera center point (valid range [0,1])
        center_point = np.array([center_equi_x_normalized, center_equi_y_normalized])
        # bounding box points left_top and bottom_right
        nfov.point1_equi = np.array([x1_normalized, y1_normalized])
        nfov.point2_equi = np.array([x2_normalized, y2_normalized])
        # remap to normal field of view
        frameRectilinear = nfov.toNFOV(self.frame, center_point, computeRectPoints=True)

        # get coordinates of points in rectilinear projection
        x1_rect = int(nfov.point1_rect[0])
        y1_rect = int(nfov.point1_rect[1])
        width_rect = int(nfov.point2_rect[0] - nfov.point1_rect[0])
        height_rect = int(nfov.point2_rect[1] - nfov.point1_rect[1])


        ##########################################################################
        ################## Tracking process initialization #######################
        ##########################################################################
        # use bounding box representation also in rectilinear
        bbox_rect = (x1_rect, y1_rect, width_rect, height_rect)

        # top left in equirectangular
        p1_equi = (int(self.bbox[0]), int(self.bbox[1]))
        # bottom right in equirectangular
        p2_equi = (int(self.bbox[0] + self.bbox[2]), int(self.bbox[1] + self.bbox[3]))

        # top left in rectilinear
        p1_rect = (bbox_rect[0], bbox_rect[1])
        # bottom right in rectilinear
        p2_rect = (bbox_rect[0] + bbox_rect[2], bbox_rect[1] + bbox_rect[3])

        # display first frame
        cv.rectangle(self.frame, p1_equi, p2_equi, (0, 255, 0), 2, 1)
        cv.imshow(self.WINDOW_NAME, self.frame)

        cv.namedWindow(self.WINDOW_NAME_RECTILINEAR)
        cv.rectangle(frameRectilinear, p1_rect, p2_rect, (255, 255, 0), 2, 1)
        cv.imshow(self.WINDOW_NAME_RECTILINEAR, frameRectilinear)

        # initialize tracker with first frame and bounding box
        self.tracker.initialize(frameRectilinear, _build_init_info(bbox_rect))

        # max fps
        videoFPS = 30
        # videoFPS = cap.get(cv.CAP_PROP_FPS) 
        # calculate the interval between frame
        interval = int(1000/videoFPS) 

        # cv.waitKey(0)

        # empiric constants for shifting/scaling in rectilinear projection - setup by experiments
        SHIFT_SLOW_X_START = 0.45 * nfov_width
        SHIFT_SLOW_Y_START = 0.45 * nfov_height
        SHIFT_FAST_X_START = 0.35 * nfov_width
        SHIFT_FAST_Y_START = 0.35 * nfov_height

        SHIFT_FAST_X = int(self.video_width / 100)
        SHIFT_FAST_Y = int(self.video_height / 100)

        SHIFT_SLOW_X = int(self.video_width / 200)
        SHIFT_SLOW_Y = int(self.video_height / 200)

        SCALEDOWN_FOV_SLOW_START_X = 0.66 * nfov_width
        SCALEDOWN_FOV_SLOW_START_Y = 0.66 * nfov_height

        SCALEDOWN_FOV_FAST_START_X = 0.8 * nfov_width
        SCALEDOWN_FOV_FAST_START_Y = 0.8 * nfov_height

        SCALEUP_FOV_SLOW_START_X = 0.25 * nfov_width
        SCALEUP_FOV_SLOW_START_Y = 0.25 * nfov_height
        
        SCALE_FOV_STEP_SLOW = 0.01
        SCALE_FOV_STEP_FAST = 0.02


        while True:
            # Read a new frame
            ok, self.frame = self.video.read()
            if not ok:
                break

            # Start timer
            timer = cv.getTickCount()

            # update center point
            if p1_rect and p2_rect and bbox_rect:
                # center of bounding box in rectilinear projection
                center_rect = [bbox_rect[0] + bbox_rect[2]/2, bbox_rect[1] + bbox_rect[3]/2]

                # SHIFTS X
                # FAST
                if center_rect[0] < SHIFT_FAST_X_START:
                    center_equi_x -= SHIFT_FAST_X
                    if center_equi_x < 0:
                        center_equi_x = self.video_width + center_equi_x
                    else:
                        center_equi_x = center_equi_x % self.video_width
                elif center_rect[0] > nfov_width - SHIFT_FAST_X_START:
                    center_equi_x += SHIFT_FAST_X
                    center_equi_x = center_equi_x % self.video_width
                # SLOW
                elif center_rect[0] < SHIFT_SLOW_X_START:
                    center_equi_x -= SHIFT_SLOW_X
                    if center_equi_x < 0:
                        center_equi_x = self.video_width + center_equi_x
                    else:
                        center_equi_x = center_equi_x % self.video_width
                elif center_rect[0] > nfov_width - SHIFT_SLOW_X_START:
                    center_equi_x += SHIFT_SLOW_X
                    center_equi_x = center_equi_x % self.video_width
                

                # SHIFTS Y
                # FAST
                if center_rect[1] < SHIFT_FAST_Y_START:
                    center_equi_y -= SHIFT_FAST_Y
                    if center_equi_y < 0:
                        center_equi_y = self.video_height + center_equi_y
                    else:
                        center_equi_y = center_equi_y % self.video_height
                elif center_rect[1] > nfov_height - SHIFT_FAST_Y_START:
                    center_equi_y += SHIFT_FAST_Y
                    center_equi_y = center_equi_y % self.video_height
                # SLOW Y
                elif center_rect[1] < SHIFT_SLOW_Y_START:
                    center_equi_y -= SHIFT_SLOW_Y
                    if center_equi_y < 0:
                        center_equi_y = self.video_height + center_equi_y
                    else:
                        center_equi_y = center_equi_y % self.video_height
                elif center_rect[1] > nfov_height - SHIFT_SLOW_Y_START:
                    center_equi_y += SHIFT_SLOW_Y
                    center_equi_y = center_equi_y % self.video_height


                # rescale FOV - enable zoom back (further from object)
                # object is close to camera/big -> increase field of view
                # FAST
                if bbox_rect[2] > SCALEDOWN_FOV_FAST_START_X or bbox_rect[3] > SCALEDOWN_FOV_FAST_START_Y:
                    if nfov.FOV[0] < 0.9:
                        nfov.FOV = [nfov.FOV[0] + SCALE_FOV_STEP_FAST, nfov.FOV[1] + SCALE_FOV_STEP_FAST]
                # SLOW
                elif bbox_rect[2] > SCALEDOWN_FOV_SLOW_START_X or bbox_rect[3] > SCALEDOWN_FOV_SLOW_START_Y:
                    if nfov.FOV[0] < 0.9:
                        nfov.FOV = [nfov.FOV[0] + SCALE_FOV_STEP_SLOW, nfov.FOV[1] + SCALE_FOV_STEP_SLOW]
                # rescale FOV - enable zoom forward (closer from object)
                elif bbox_rect[2] < SCALEDOWN_FOV_SLOW_START_X and bbox_rect[3] < SCALEDOWN_FOV_SLOW_START_Y:
                    # object is small and field of view is large 
                    if nfov.FOV[0] > 0.6:
                        # decrease field of view
                        nfov.FOV = [nfov.FOV[0] - SCALE_FOV_STEP_SLOW, nfov.FOV[1] - SCALE_FOV_STEP_SLOW]

            # normalize center point in [0,1]
            center_equi_x_normalized = center_equi_x / self.video_width
            center_equi_y_normalized = center_equi_y / self.video_height
            # camera center point (valid range [0,1])
            center_point = np.array([center_equi_x_normalized, center_equi_y_normalized])  

            # new frame to rectilinear/normal field of view
            frameRectilinear = nfov.toNFOV(self.frame, center_point)

            # Get tracked bbox
            out = self.tracker.track(frameRectilinear)
            state = [int(s) for s in out['target_bbox'][1]]

            # bbox_rect should be same as state
            bbox_rect = state

            # Calculate Frames per second (FPS)
            fps = cv.getTickFrequency() / (cv.getTickCount() - timer)

            # draw bounding box
            if state[0] and state[1] and state[2] and state[3]:
                # Tracking success in rectilinear
                p1_rect = (state[0], state[1])
                p2_rect = (state[0] + state[2], state[1] + state[3])

                # store points to nfov instance
                nfov.point1_rect = [p1_rect[0], p1_rect[1]]
                nfov.point2_rect = [p2_rect[0], p2_rect[1]]
                # draw bounding box to rectilinear frame
                cv.rectangle(frameRectilinear, p1_rect, p2_rect, (255, 255, 0), self.RECTANGLE_BORDER_PX, 1)

                # equirectangular
                # compute corresponding points of rectilinear bounding box in equirectangular projection 
                nfov.computeEquirectangularBbox(bbox_width=round(bbox_rect[2]), bbox_height=round(bbox_rect[3]))
                # bbox points top left and right bottom in equirectangular projection
                p1_equi = (int(round(nfov.point1_equi[0] * self.video_width)), int(round(nfov.point1_equi[1] * self.video_height)))
                p2_equi = (int(round(nfov.point2_equi[0] * self.video_width)), int(round(nfov.point2_equi[1] * self.video_height)))

                # create custom equirectangular bounding box instance
                bb = BoundingBox(p1_equi, p2_equi, self.video_width)
                bb.is_annotated = True
                self.result_bounding_boxes.append(bb)

                # draw bounding box to original equirectangular frame
                self._drawBoundingBox(self.video_width, p1_equi, p2_equi, bb, (0, 255, 0), self.RECTANGLE_BORDER_PX)
            else:                
                # tracking failure
                cv.putText(self.frame, "Tracking failure detected", self.TEXT_ROW4_POS, cv.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 0, 255), self.FONT_WEIGHT)
                
                # reinit points
                p1_rect = None
                p2_rect = None
                p1_equi = None
                p2_equi = None

                # new instance of bounding box
                bb = BoundingBox(None, None, self.video_width)
                bb.is_annotated = False
                self.result_bounding_boxes.append(bb)

            
            # Display tracker type on frame
            cv.putText(self.frame, self.name.upper() + " Tracker", self.TEXT_ROW1_POS, cv.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 200, 250), self.FONT_WEIGHT)
            # Display FPS on frame
            cv.putText(self.frame, "Video   FPS : " + str(videoFPS), self.TEXT_ROW2_POS, cv.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 250, 0), self.FONT_WEIGHT)
            cv.putText(self.frame, "Tracker FPS : " + str(int(fps)), self.TEXT_ROW3_POS, cv.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 250, 0), self.FONT_WEIGHT)
            
            # Display result
            cv.imshow(self.WINDOW_NAME, self.frame)
            cv.imshow(self.WINDOW_NAME_RECTILINEAR, frameRectilinear)
            

            # waitKey time computing
            # time in ms
            time = int(1000 * (cv.getTickCount() - timer) / cv.getTickFrequency())

            waitMiliseconds = 1
            if (time >= interval):
                waitMiliseconds = 1
            else:
                waitMiliseconds = interval - time
            
            k = cv.waitKey(waitMiliseconds) & 0xff
            # Exit if 'Esc' or 'q' key is pressed
            if k == 27 or k == ord("q"): 
                break


        # always save tracker result
        self._saveResults()

        self.video.release()
        cv.destroyAllWindows()



    # method for start tracking without any modifications
    def run_video_default(self, optional_box=None, debug=None, visdom_info=None):
        params = self.get_parameters()

        debug_ = debug
        if debug is None:
            debug_ = getattr(params, 'debug', 0)
        params.debug = debug_

        params.tracker_name = self.name
        params.param_name = self.parameter_name
        self._init_visdom(visdom_info, debug_)

        multiobj_mode = getattr(params, 'multiobj_mode', getattr(self.tracker_class, 'multiobj_mode', 'default'))

        if multiobj_mode == 'default':
            self.tracker = self.create_tracker(params)
            if hasattr(self.tracker, 'initialize_features'):
                self.tracker.initialize_features()
        elif multiobj_mode == 'parallel':
            self.tracker = MultiObjectWrapper(self.tracker_class, params, self.visdom, fast_load=True)
        else:
            raise ValueError('Unknown multi object mode {}'.format(multiobj_mode))

        ###########################################################################
        #############         Part of custom modifications            #############
        ###########################################################################
        ########## 1) Video Checking ##########
        # Read video
        self.video = cv.VideoCapture(self.video_path)
        # Exit if video not opened.
        if not self.video.isOpened():
            print("Could not open video")
            print(help)
            sys.exit(-1)

        # Read first frame.
        ok, self.frame = self.video.read()
        if not ok:
            print("Error - Could not read a video file")
            sys.exit(-1)

        # save video width/height to global variables
        self.video_width = int(self.video.get(cv.CAP_PROP_FRAME_WIDTH))
        self.video_height = int(self.video.get(cv.CAP_PROP_FRAME_HEIGHT))

        # correct format of initialization bbox
        def _build_init_info(box):
            return {'init_bbox': OrderedDict({1: box}), 'init_object_ids': [1, ], 'object_ids': [1, ], 'sequence_object_ids': [1, ]}


        ########## 2) Setup opencv window ##########
        # resize window (lets define max width is 1600px)
        if self.video_width < 1600:
            cv.namedWindow(self.WINDOW_NAME)
        else:
            cv.namedWindow(self.WINDOW_NAME, cv.WINDOW_NORMAL | cv.WINDOW_KEEPRATIO)
            whRatio = self.video_width / self.video_height
            if whRatio == 2:
                # pure equirectangular 2:1
                cv.resizeWindow(self.WINDOW_NAME, 1600, 800)
            else:
                # default 16:9
                cv.resizeWindow(self.WINDOW_NAME, 1600, 900)

            scaleFactor = self.video_width / 1600
            self.RECTANGLE_BORDER_PX = int(self.RECTANGLE_BORDER_PX * scaleFactor)
            self.FONT_SCALE = self.FONT_SCALE * scaleFactor
            self.FONT_WEIGHT = int(self.FONT_WEIGHT * scaleFactor) + 1
            self.TEXT_ROW1_POS = (int(self.TEXT_ROW1_POS[0] * scaleFactor), int(self.TEXT_ROW1_POS[1] * scaleFactor))
            self.TEXT_ROW2_POS = (int(self.TEXT_ROW2_POS[0] * scaleFactor), int(self.TEXT_ROW2_POS[1] * scaleFactor))
            self.TEXT_ROW3_POS = (int(self.TEXT_ROW3_POS[0] * scaleFactor), int(self.TEXT_ROW3_POS[1] * scaleFactor))
            self.TEXT_ROW4_POS = (int(self.TEXT_ROW4_POS[0] * scaleFactor), int(self.TEXT_ROW4_POS[1] * scaleFactor))

        # use copy of frame to be shown in window
        frame_disp = self.frame.copy()

        ########## 3) Initialation of bounding box ##########
        # Set up initial bounding box
        self.bbox = None
        self.result_bounding_boxes = []
        self.gt_bounding_boxes = []
        if self.groundtruth_path:
            # use first bounding box from given groundtruth
            self.gt_bounding_boxes = self.parser.parseGivenDataFile(self.groundtruth_path, self.video_width)

            if len(self.gt_bounding_boxes) > 0:
                bb1 = self.gt_bounding_boxes[0]
                if bb1.is_annotated:
                    self.bbox = (bb1.get_point1_x(), bb1.get_point1_y(), bb1.get_width(), bb1.get_height())
                    self.result_bounding_boxes.append(bb1)
                else:
                    print("Error - Invalid first frame annotation from file: '" + self.groundtruth_path + "'")
                    sys.exit(-1)
        else:
            # using opencv select ROI
            cv.putText(frame_disp, 'Select target ROI and press ENTER', self.TEXT_ROW1_POS, cv.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 200, 250), self.FONT_WEIGHT)

            x, y, w, h = cv.selectROI(self.WINDOW_NAME, frame_disp, fromCenter=False)
            self.bbox = [x, y, w, h]

            # save it to result list
            p1 = (int(self.bbox[0]), int(self.bbox[1]))
            p2 = (int(self.bbox[0] + self.bbox[2]), int(self.bbox[1] + self.bbox[3]))
            # new instance of bounding box
            bb1 = BoundingBox(p1, p2, self.video_width)
            bb1.is_annotated = True
            self.result_bounding_boxes.append(bb1)

        if not(self.bbox) or self.bbox == (0,0,0,0):
            print("Error - Invalid first frame annotation")
            sys.exit(-1)


        ########## 4) Tracking process ##########
        # prints just basic guide and info
        print("--------------------------------------------------------------------")
        print("pytracking default tracking process has started...")
        print("Tracker  : " + self.name.upper())
        print("Frame #1 : " + str(self.bbox))
        print("Press 'Esc' or 'Q' key to exit")
        print("--------------------------------------------------------------------")

        # display first frame
        cv.imshow(self.WINDOW_NAME, frame_disp)

        # initialize tracker with first frame and bounding box
        self.tracker.initialize(self.frame, _build_init_info(self.bbox))

        # if you want to have the FPS according to the video then uncomment this code
        # fps = cap.get(cv.CAP_PROP_FPS)
        videoFPS = 30
        # calculate the interval between frame
        interval = int(1000/videoFPS) 


        while True:
            # Read a new frame
            ok, self.frame = self.video.read()
            if not ok:
                break

            # Start timer
            timer = cv.getTickCount()

            # Get tracked bbox
            out = self.tracker.track(self.frame)
            state = [int(s) for s in out['target_bbox'][1]]

            # Calculate Frames per second (FPS)
            fps = cv.getTickFrequency() / (cv.getTickCount() - timer)

            # draw bounding box
            if state[0] and state[1] and state[2] and state[3]:
                # Tracking success
                p1 = (state[0], state[1])
                p2 = (state[0] + state[2], state[1] + state[3])

                p1 = self._checkBoundsOfPoint(p1)
                p2 = self._checkBoundsOfPoint(p2)

                # new instance of bounding box
                bb = BoundingBox(p1, p2, self.video_width)
                bb.is_annotated = True
                self.result_bounding_boxes.append(bb)

                # draw bounding box to original frame
                self._drawBoundingBox(self.video_width, p1, p2, bb, (0, 255, 0), self.RECTANGLE_BORDER_PX)
            else:                
                # tracking failure
                cv.putText(self.frame, "Tracking failure detected", self.TEXT_ROW4_POS, cv.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 0, 255), self.FONT_WEIGHT)
                
                # new instance of bounding box
                bb = BoundingBox(None, None, self.video_width)
                bb.is_annotated = False
                self.result_bounding_boxes.append(bb)

            
            # Display tracker type on frame
            cv.putText(self.frame, self.name.upper() + " Tracker", self.TEXT_ROW1_POS, cv.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 200, 250), self.FONT_WEIGHT)
            # Display FPS on frame
            cv.putText(self.frame, "Video   FPS : " + str(videoFPS), self.TEXT_ROW2_POS, cv.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 250, 0), self.FONT_WEIGHT)
            cv.putText(self.frame, "Tracker FPS : " + str(int(fps)), self.TEXT_ROW3_POS, cv.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 250, 0), self.FONT_WEIGHT)
            # Display result
            cv.imshow(self.WINDOW_NAME, self.frame)
            

            # waitKey time computing
            # time in ms
            time = int(1000 * (cv.getTickCount() - timer) / cv.getTickFrequency())

            waitMiliseconds = 1
            if (time >= interval):
                waitMiliseconds = 1
            else:
                waitMiliseconds = interval - time
            
            k = cv.waitKey(waitMiliseconds) & 0xff
            # Exit if 'Esc' or 'q' key is pressed
            if k == 27 or k == ord("q"): 
                break


        # always save tracker result
        self._saveResults()

        self.video.release()
        cv.destroyAllWindows()



