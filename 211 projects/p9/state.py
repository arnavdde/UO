class State:
    def __init__(self, x=0, y=0, angle=0):
        self.x = x
        self.y = y
        self.angle = angle

    def __str__(self):
        return f"({self.x}, {self.y}, {self.angle})"
    
    def __repr__(self):
        return self.__str__()

    def set_state(self, t):
        self.x = t.xcor()
        self.y = t.ycor()
        self.angle = t.heading()

class Stack:
    def __init__(self):
        self.stuff = []

    def push(self, item):
        self.stuff.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stuff.pop()
        else:
            return IndexError("Stack is empty")
        
    def is_empty(self):
        return len(self.stuff) == 0