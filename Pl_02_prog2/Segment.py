from Point import Point


class Segment:

    def __init__(self, point_1, point_2, color):
        self._point_a = point_1
        self._point_b = point_2
        self._color = color 


    def setPointA(self, obj_to_set):
        self._point_a = obj_to_set


    def setPointB(self, obj_to_set):
        self._point_b = obj_to_set


    def getPointA(self):
        return (self._point_a.getX(), self._point_a.getY())

    
    def getPointB(self):
        return (self._point_b.getY(), self._point_b.getY())

    
    def length(self):
        return self._point_a.distance(self._point_b)