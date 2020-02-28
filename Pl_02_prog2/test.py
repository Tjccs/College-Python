from Point import Point
from Segment import Segment
from Polygon import Polygon

point = Point(1, 2)
point_2 = Point(2, 3)
segment = Segment(point, point_2, "red")

point_3 = Point(3,7)
point_4 = Point(7,9)
seg_2 = Segment(point_3, point_4, "red")

point_3 = Point(9,11)
point_4 = Point(11,13)
seg_3 = Segment(point_3, point_4, "red")


point_5 = Point(13,16)
point_6 = Point(16,1)
seg_4 = Segment(point_5, point_6, "red")

pol = Polygon([segment, seg_2, seg_3, seg_4])
print(f'Polygon perimeter: {pol.perimeter()}')