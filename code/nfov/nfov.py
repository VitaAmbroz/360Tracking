#################################################################################################
# Visual object tracking in panoramic video
# Master thesis at Brno University of Technology - Faculty of Information Technology
# Author:       Vít Ambrož (xambro15@stud.fit.vutbr.cz)
# Supervisor:   Doc. Ing. Martin Čadík, Ph.D.
# Module:       nfov.py
# Description:  Modified implementation of rectilinear/gnomopic mapping (equirectangular to normal field of view)
# Source:       http://blog.nitishmutha.com/equirectangular/360degree/2017/06/12/How-to-project-Equirectangular-image-to-rectilinear-view.html
#               https://github.com/NitishMutha/equirectangular-toolbox
#################################################################################################

# Copyright 2017 Nitish Mutha (nitishmutha.com)

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#   http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from cv2 import cv2
from math import pi
import numpy as np

class NFOV():
    def __init__(self, height=400, width=800):
        # default FOV 90°
        self.FOV = [0.5, 0.5]
        self.PI = pi
        self.PI_2 = pi * 0.5
        self.PI2 = pi * 2.0
        # width and height
        self.height = height
        self.width = width

        # sample points to width*height arrray
        self.screen_points = self._get_screen_img()
        # other arrays used in toNFOV method
        self.convertedScreenCoord = None
        self.sphericalCoord = None
        self.sphericalCoordReshaped = None

        # center point of normal field of view/rectilinear
        self.cp = [0,0]
        # bbox top left and bottom right points in rectilinear
        self.point1_rect = [0,0]
        self.point2_rect = [0,0]
        # bbox top left and bottom right points in equirectangular
        self.point1_equi = [0,0]
        self.point2_equi = [0,0]


    def _get_coord_rad_point(self, point):
        return (point * 2 - 1) * np.array([self.PI, self.PI_2])

    def _get_coord_rad_screen_points(self):
        return (self.screen_points * 2 - 1) * np.array([self.PI, self.PI_2]) * (np.ones(self.screen_points.shape) * self.FOV)

    def _get_screen_img(self):
        # sample grid with self.width * self.height points
        xx, yy = np.meshgrid(np.linspace(0, 1, self.width), np.linspace(0, 1, self.height))
        return np.array([xx.ravel(), yy.ravel()]).T

    def _calcSphericaltoGnomonic(self, convertedScreenCoord):
        x = convertedScreenCoord.T[0]
        y = convertedScreenCoord.T[1]

        rou = np.sqrt(x ** 2 + y ** 2)
        c = np.arctan(rou)
        sin_c = np.sin(c)
        cos_c = np.cos(c)

        lat = np.arcsin(cos_c * np.sin(self.cp[1]) + (y * sin_c * np.cos(self.cp[1])) / rou)
        lon = self.cp[0] + np.arctan2(x * sin_c, rou * np.cos(self.cp[1]) * cos_c - y * np.sin(self.cp[1]) * sin_c)

        lat = (lat / self.PI_2 + 1.) * 0.5
        lon = (lon / self.PI + 1.) * 0.5

        return np.array([lon, lat]).T


    ########################### Stackexchange atrtibution ##############################################
    # https://codereview.stackexchange.com/questions/28207/finding-the-closest-point-to-a-list-of-points
    # Asked by dassouki:    https://codereview.stackexchange.com/users/190/dassouki
    # Answeerd by jaime:    https://codereview.stackexchange.com/users/20894/jaime
    # methods for computing the closest point in array of points
    def _closest_point(self, point, points):
        points = np.asarray(points)
        dist_2 = np.sum((points - point)**2, axis=1)
        return np.argmin(dist_2)

    def _closest_point2(self, point, points):
        points = np.asarray(points)
        deltas = points - point
        dist_2 = np.einsum('ij,ij->i', deltas, deltas)
        return np.argmin(dist_2)
    ####################################################################################################


    def toNFOV(self, frame, center_point, computeRectPoints=False):
        # equirectangular frame
        self.frame = frame
        self.frame_height = frame.shape[0]
        self.frame_width = frame.shape[1]
        self.frame_channel = frame.shape[2]
        # point in equirectangular projection normalized to [0,1] -> center point of new rectilinear projection
        self.cp = self._get_coord_rad_point(point=center_point)

        # radians mapped to self.frame_width * self.frame_height grid
        self.convertedScreenCoord = self._get_coord_rad_screen_points()
        # spherical points to be shown in new rectiliner projection (normalized to [0,1])
        self.sphericalCoord = self._calcSphericaltoGnomonic(self.convertedScreenCoord)
        
        # computing bounding box points
        if computeRectPoints and len(self.sphericalCoord):
            # compute 2 given points in new rectilinear/normal field of view 
            indexPt1 = self._closest_point2(self.point1_equi, self.sphericalCoord)
            self.point1_rect = [int(indexPt1 % self.width), int(round(indexPt1 / self.width))]

            indexPt2 = self._closest_point2(self.point2_equi, self.sphericalCoord)
            self.point2_rect = [int(indexPt2 % self.width), int(round(indexPt2 / self.width))]

        # reshape to self.height arrays - each contains self.width arrays - each contains 2D arrays(points)
        self.sphericalCoordReshaped = self.sphericalCoord.reshape(self.height, self.width, 2).astype(np.float32) % 1

        # remap to out frame to be shown
        out = cv2.remap(self.frame, (self.sphericalCoordReshaped[..., 0] * self.frame_width), (self.sphericalCoordReshaped[..., 1] * self.frame_height), interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_WRAP)
        return out

    
    # check if given point is in interval [0,self.width] and [0,self.height]
    def _checkBoundsOfPoint(self, point):
        if point[0] < 0: 
            point[0] = 0
        elif point[0] > self.width - 1: 
            point[0] = self.width - 1
        
        if point[1] < 0: 
            point[1] = 0
        elif point[1] > self.height - 1:
            point[1] = self.height - 1

        return point

    def computeEquirectangularBbox(self, bbox_width: int, bbox_height: int):
        if len(self.sphericalCoord) and self.point1_rect and self.point2_rect:
            # get 4 centers of bounding box rectangle
            left_center_point = [self.point1_rect[0], round(self.point1_rect[1] + bbox_height/2)]
            top_center_point = [round(self.point1_rect[0] + bbox_width/2), self.point1_rect[1]]
            right_center_point = [self.point2_rect[0], round(self.point1_rect[1] + bbox_height/2)]
            bottom_center_point = [round(self.point1_rect[0] + bbox_width/2), self.point2_rect[1]]

            # some tracker could predict point out of image width/height (caucht in experiments)
            left_center_point = self._checkBoundsOfPoint(left_center_point)
            top_center_point = self._checkBoundsOfPoint(top_center_point)
            right_center_point = self._checkBoundsOfPoint(right_center_point)
            bottom_center_point = self._checkBoundsOfPoint(bottom_center_point)

            # get spherical coordinates of 4 centers
            left_center_equi = self.sphericalCoord[left_center_point[1]*self.width + left_center_point[0]]
            top_center_equi = self.sphericalCoord[top_center_point[1]*self.width + top_center_point[0]]
            right_center_equi = self.sphericalCoord[right_center_point[1]*self.width + right_center_point[0]]
            bottom_center_equi = self.sphericalCoord[bottom_center_point[1]*self.width + bottom_center_point[0]]

            # use correct x,y for equirectangular bounding box
            self.point1_equi = [left_center_equi[0], top_center_equi[1]]
            self.point2_equi = [right_center_equi[0], bottom_center_equi[1]]