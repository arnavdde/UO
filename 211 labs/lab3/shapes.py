from math import *

class Shape3D:
    def __init__(self):
        raise NotImplementedError("Abstract class cannot be instantiated")

    def volume(self) -> float:
        raise NotImplementedError("Not implemented for abstract class")

    def area(self) -> float:
        raise NotImplementedError("Not implemented for abstract class")
    
    def print_info(self):
        return f"Area: {self.area()}, Volume: {self.volume()}"
    

class Cylinder(Shape3D):
    def __init__(self, radius:float, height:float):
        self.radius = radius
        self.height = height

    def volume(self) -> float:
        return pi * (self.radius ** 2) * self.height

    def area(self) -> float:
        return 2 * pi * (self.radius ** 2) + 2 * pi * self.radius * self.height
        

class Cuboid(Shape3D):
    def __init__(self, width:float, length:float, height:float):
        self.width = width
        self.height = height
        self.length = length

    def volume(self, width, height, length) -> float:
        return self.width * self.length * self.height

    def area(self) -> float:
        return 2 * self.width * self.length + 2 * self.length * self.height * 2 * self.width


class Cube(Cuboid):
    def __init__(self, width: float):
        super().__init__(width, width, width)

