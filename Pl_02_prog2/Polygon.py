from Segment import Segment

class Polygon:

    def __init__(self, list_of_segments):
        """ Define a polygon using segment objects
        Requires: A list of segments ordered, with all segments conecting with the last one
        Ensures: A polygon constructed with segments
        """
        self._list_of_segments = list_of_segments

    
    def perimeter(self):
        total_perimeter = 0
        for segment in self.getPolygon():
            total_perimeter += segment.length()
        return total_perimeter


    def setPolygon(self, new_polygon):
        self._list_of_segments = new_polygon


    def getPolygon(self):
        return self._list_of_segments