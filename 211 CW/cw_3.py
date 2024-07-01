from ast import main
from numbers import *
from math import *



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, d:"Point") -> "Point":
        x = self.x + d.x
        y = self.y + d.y
        return Point(x, y)
    
    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other:"Point") -> Number:
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx*dy + dy*dy)
    
    # def __str__(self) ->str:
    #     return f"Rect({str(self.min_pt)}), {str(self.max_pt)})"
    
    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"
    

class Rect:
    '''2 corners'''
    def __init__(self, p1:Point, p2:Point):
        '''initialize non adj corners (low left, up right)'''
        self.ll = Point(min(p1.x, p2.x), min(p1.y, p2.y))
        self.ur = Point(max(p1.x, p2.x), max(p1.y, p2.y))
    
    def __eq__(self, other: "Rect") -> bool:
        return self.ll == other.ll and self.ur == other.ur
    
    # def translate(self, delta: Point) -> "Rect":
    #     self.ll = self.ll + delta.x
    #     self.ur = self.y=ur + delta.y

    def __repr__(self) -> str:
        return "Rect({}, {})".format(self.ll, self.ur)

    def area(self) -> int:
        return (self.ur.x - self.ll.x) * (self.ur.y - self.ll.y)
    
    
class Square(Rect):
    '''rect, defined by a corner and lenght of a side'''
    def __init__(self, ll:Point, side:int):
        self.ll = ll
        self.ur = Point(ll.x + side, ll.y + side)
        
if __name__ == "__main__":
    
    # p1 = Point(3, 5)
    # print(p1)
    # print(p1.dist(Point(0,0)))

    r1 = Rect(Point(0,0), Point(3,4))
    print(r1)
    print(r1.area())
    # r2 = r1.translate(Point(1,1))
    # print(r2)
