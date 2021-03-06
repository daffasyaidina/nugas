class Circle:
    def __init__(self,radius = 1.0,color = "red"):
        self.__radius = radius * 2
        self.__color = str(color)    
    def getRadius(self):
        return self.__radius   
    def getColor(self):
        return self.__color   
    def getArea(self):
        return ((3.14)*(self.getRadius()**2))
    def toString(self):
        return f"Radius: {self.getRadius()}" + "\n" + f"Color: {self.getColor()}"
    def setRadius(self, new_radius):
        self.__radius = new_radius * 2
    def setColor(self, new_color):
        self.__color = new_color
   
class Cylinder(Circle):
    def __init__(self, radius, color, height = 1.0):
        super().__init__(radius, color)
        self.__height = height * 2
    def getHeight(self):
        return self.__height
    def setHeight(self, new_height):
        self.__height = new_height * 2
    def getVolume(self):
         return (3.14)*((self.getRadius())**2)* self.getHeight()
         