#################################################################################################
# Visual object tracking in panoramic video
# Master thesis at Brno University of Technology - Faculty of Information Technology
# Author:       Vít Ambrož (xambro15@stud.fit.vutbr.cz)
# Supervisor:   Doc. Ing. Martin Čadík, Ph.D.
# Module:       boundingbox.py
# Description:  Simple representation of bounding box for object annotation
#               Supports object left/right border crossing in equirectangular panorama 
#################################################################################################

class BoundingBox():
    """
    Simple representation of bounding box for object annotation.
    Supports of object left/right border crossing in equirectangular panorama.
    """
    def __init__(self, point1, point2, frame_width):
        self.point1 = point1
        self.point2 = point2
        self.frame_width = frame_width
        self.is_annotated = False
        self.frame_copy = None

    def get_point1_x(self):
        """X coordinate of bounding box TOP LEFT corner"""
        return self.point1[0]

    def get_point1_y(self):
        """Y coordinate of bounding box TOP LEFT corner"""
        return self.point1[1]

    def get_point2_x(self):
        """X coordinate of bounding box BOTTOM RIGHT corner"""
        return self.point2[0]

    def get_point2_y(self):
        """Y coordinate of bounding box BOTTOM RIGHT corner"""
        return self.point2[1]

    def get_x1(self):
        """X coordinate of bounding box TOP LEFT corner"""
        return self.point1[0]

    def get_y1(self):
        """Y coordinate of bounding box TOP LEFT corner (in anottation toll user could anotate bottom left corner)"""
        if self.point1[1] < self.point2[1]:
            return self.point1[1]
        else: 
            return self.point2[1]

    def is_on_border(self):
        """Defines if bounding box is on left<->right border in equirectangular"""
        return self.get_point2_x() < self.get_point1_x()

    def get_width(self):
        """Width of bounding box"""
        if self.is_on_border():
            return (self.frame_width - self.get_point1_x()) + self.get_point2_x()
        else:
            return self.get_point2_x() - self.get_point1_x()

    def get_height(self):
        """Height of bounding box"""
        return abs(self.get_point2_y() - self.get_point1_y())
