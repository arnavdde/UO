# def move(p, d):
#     '''points move in space'''
#     x, y = p
#     dx, dy = d
#     return(x+dx, y+dy)


class Point:
    ''' an x y coordiante pair'''

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, d):
        '''(x,y).move(dx,dy) = (x+dx,y+dy)'''
        x = self.x + d.x
        y = self.y + d.y
        return(Point(x, y))
    

if __name__ == '__main__':
    p = Point(3,4)
    v = Point(5,6)
    m = p.move(v)
    print(f"{p} + {v} = {m}")

    assert m.x == 8 and m.y == 10
    # if so, the test succeeds, else, we get an AssertionError