#################################################################################################
# Visual object tracking in panoramic video
# Master thesis at Brno University of Technology - Faculty of Information Technology
# Author:       Vít Ambrož (xambro15@stud.fit.vutbr.cz)
# Supervisor:   Doc. Ing. Martin Čadík, Ph.D.
# Module:       boundingbox.py
# Description:  Simple representation of bounding box for object annotation
#               Basic support of object left/right border crossing in equirectangular panorama 
#################################################################################################

class BoundingBox():
    def __init__(self, point1, point2, frame_width):
        self.point1 = point1
        self.point2 = point2
        self.frame_width = frame_width
        self.is_annotated = False
        self.frame_copy = None

    def get_point1_x(self):
        return self.point1[0]

    def get_point1_y(self):
        return self.point1[1]

    def get_point2_x(self):
        return self.point2[0]

    def get_point2_y(self):
        return self.point2[1]

    def is_on_border(self):
        return self.get_point2_x() < self.get_point1_x()

    # this attributes corresponds to ground truth rectangle (x1, y1, width, height)
    def get_x1(self):
        return self.point1[0]

    def get_y1(self):
        # user could annotate TOP LEFT or also BOTTOM LEFT
        if self.point1[1] < self.point2[1]:
            return self.point1[1]
        else: 
            return self.point2[1]

    def get_width(self):
        if self.is_on_border():
            return (self.frame_width - self.get_point1_x()) + self.get_point2_x()
        else:
            return self.get_point2_x() - self.get_point1_x()

    def get_height(self):
        return abs(self.get_point2_y() - self.get_point1_y())

  