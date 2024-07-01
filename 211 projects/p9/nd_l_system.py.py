import random
from state import *
import turtle

class LSystem:
    def __init__(self, axiom, rules, angle, step, n=3, starting_pos=(-200, 0), starting_angle=0, color='blue'):
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
        new_word = ''
        for char in word:
            if char in self.rules:
                rule = self.rules[char]
                if isinstance(rule, list):
                    total_prob = sum(r[0] for r in rule)
                    rand_prob = random.random() * total_prob
                    cumulative_prob = 0
                    for prob, subst in rule:
                        cumulative_prob += prob
                        if cumulative_prob >= rand_prob:
                            new_word += subst
                            break
                else:
                    new_word += rule
            else:
                new_word += char
        return new_word    

    def iterate(self):
        current_string = self.axiom
        for i in range(self.n):
            current_string = self.replace(current_string)
        self.commands = current_string

    def draw(self):
        t = turtle.Turtle()
        s = turtle.Screen()
        t.color(self.color)
        t.penup()
        t.goto(self.starting_pos)
        t.pendown()
        t.setheading(self.starting_angle)
        for cmd in self.commands:
            if cmd == 'F':
                t.forward(self.step)
            elif cmd == 'f':
                t.penup()
                t.forward(self.step)
                t.pendown()
            elif cmd == '+':
                t.left(self.angle)
            elif cmd == '-':
                t.right(self.angle)
            elif cmd == '[':
                state = State(t.xcor(), t.ycor(), t.heading())
                self.pos.push(state)
            elif cmd == ']':
                state = self.pos.pop()
                t.penup()
                t.goto(state.x, state.y)
                t.setheading(state.angle)
                t.pendown()
        s.exitonclick()

    def plot(self):
        self.iterate()
        self.draw()

random.seed(42)

if __name__ == "__main__":


    ls_system = LSystem(
        axiom="F",
        rules={"F": [(0.33, "F[+F]F[-F]F"), (0.33, "F[-F]F"), (0.34, "F[+F]F")]},
        angle=25.7,
        step=10,
        n=4
    )
    ls_system.plot()