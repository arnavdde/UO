from state import *
import turtle

class LSystem:
    """
    Represents an L-System with its axiom, rules, rewriting, and drawing methods.
    """
    def __init__(self, axiom, rules, angle, step, n=3, starting_pos=(-200, 0), starting_angle=0, color='blue') -> None:
        self.axiom = axiom
        self.rules = rules
        self.angle = angle
        self.step = step
        self.n = n
        self.starting_pos = starting_pos
        self.starting_angle = starting_angle
        self.color = color
        self.commands = ''
        self.pos = Stack()
        
    def replace(self, word):
        new = ''
        for i in range(len(word)):
            if word[i] in self.rules:
                new += self.rules[word[i]]
            else:
                new += word[i]
        return new    

    def iterate(self):
        current_string = self.axiom
        for i in range(self.n):
            current_string = self.replace(current_string)
        self.commands = current_string
        return None

    def draw(self):
        turtle.setup(800, 600)  # Set the window size
        t = turtle.Turtle()
        s = turtle.Screen()
        t.color(self.color)
        t.penup()
        t.goto(self.starting_pos)
        t.pendown()
        t.setheading(self.starting_angle)
        for c in self.commands:
            if c == 'F':
                t.forward(self.step)
            elif c == 'f':
                t.penup()
                t.forward(self.step)
                t.pendown()
            elif c == '+':
                t.left(self.angle)
            elif c == '-':
                t.right(self.angle)
            elif c == '[':
                state = State()
                state.set_state(t)
                self.pos.push(state)
            elif c == ']':
                state = self.pos.pop()
                t.penup()
                t.goto(state.x, state.y)
                t.setheading(state.angle)
                t.pendown()
        s.exitonclick()

    def plot(self):
        self.iterate()
        self.draw()

if __name__ == "__main__":
    ls1 = LSystem(
        axiom="-L",
        rules={"L": "LF+RFR+FL-F-LFLFL-FRFR+", "R": "- LFLF+RFRFR+F+RF-LFL-FR"},
        angle=90,
        step=10,
        n=3,
    )
    ls1.plot()