import math
class Point:

    def __init__(self, x = 0, y = 0):
      self.x = x
      self.y = y

    def __str__(self):
        return "x:"+str(self.x)+" y:"+str(self.y)

    def distanciaOutroPonto (self, outroPonto):
        try:
            if not isinstance(outroPonto, Point):
                raise TypeError("not a point")
            else:

                dif = math.sqrt(((outroPonto.x + self.x)**2) + (outroPonto.y + self.y)**2)
                result = str(dif)
                return result

        except TypeError:
            print("Erro")

    def distanciaOrigem(self):
        result = self.distanciaOutroPonto(Point(0,0))
        return result


class Point3D(Point):

    def __init__ (self, x = 0, y = 0, z=0):

        if not isinstance(x, (int)) or not isinstance(y, (int)) or not isinstance(z, (int)):
            raise IOError("Variables not ints")
        super(Point3D, self).__init__(x, y)
        self.z = z

    def __str__(self):
        return "x:"+str(self.x)+" y:"+str(self.y)+" z:"+str(self.z)

    def distanciaOutroPonto (self, outroPonto):
        dif = math.sqrt(((outroPonto.x + self.x)**2) + (outroPonto.y + self.y)**2 + (outroPonto.z + self.z)**2)
        result = str(dif)
        return result

    def distanciaOrigem(self):
        result = self.distanciaOutroPonto(Point3D(0,0,0))
        return result

class Circulo:

    def __init__(self, centro, raio):
        if not isinstance(centro, (Point)):
            raise IOError("Variables not a Point")
        else:
            self.raio = raio

    def diametro():
        return self.raio*2

    def area():
        return math.pi*(self.raio**2)
      
class CircleWithProperties:
  
  def __init__(self, centro, raio):
        self.centro = centro
        self.__raio = raio
        
  @property
  def raio(self):
        return self.raio
  
  @property
  def centro(self):
        return self.centro
  
  @centro.setter
  def centro(self, outroCentro):
        if not isinstance(outroCentro, (Point)):
          raise ValueError("Invalid type argument")
        else:
          self.__centro = outroCentro
  
  @property      
  def diametro(self):
        return self.raio*2
      
  @property
  def area(self):
        return math.pi*(self.raio**2)
      
       
if __name__ == '__main__':
        b = Point(2,3)
        a = Point(1,1)

        c = Point3D(1,0,1)
        d = Point3D(0,0,0)

        print(c.distanciaOutroPonto(d))
