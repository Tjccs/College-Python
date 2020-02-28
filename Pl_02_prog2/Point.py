import math

class Point:
    """
    Point in the plane.
    """
    
    def __init__(self, x = 0, y = 0):
        '''
        Creates a point at the center of the axis
        '''
        self._x = x
        self._y = y


    def setX(self, ex):
        '''
        Sets the x coordinate of the point.
        Requires: ex is an int, the coordinate in the x-axis
        Ensures: self.getX() == ex
        '''
        self._x=ex
    

    def setY(self, wye):
        '''
        Sets the y coordinate of the point.
        Requires: wye is an int, the coordinate in the y-axis
        Ensures: self.getY() == wye
        '''
        self._y=wye


    def getX(self):
        '''
        The x coordinate of the point
        '''
        return self._x
    
    
    def getY(self):
        '''
        The y coordinate of the point
        '''
        return self._y

    def shift(self, xInc, yInc):
        self.setX(self.getX() + xInc) , self.setY(self.getY() + yInc)


    def distance(self, otherPoint):
        delta_x = otherPoint.getX() - self.getX()
        delta_y = otherPoint.getY() - self.getY()

        return math.sqrt(delta_x**2 + delta_y**2)