from Polygon import Polygon

class Scene:

    def __init__(self, list_of_polygons):
        self._list_of_polygons = list_of_polygons
    
    
    def setScene(self, new_scene):
        self._list_of_polygons = new_scene

    
    def getScene(self):
        return self._list_of_polygons

    
    def scenePerimeter(self):
        scene_per = 0
        for polygon in self.getScene():
            scene_per += polygon.perimeter()
        return scene_per
        # return [sum(polygon.perimeter()) for polygon in self.getScene()]