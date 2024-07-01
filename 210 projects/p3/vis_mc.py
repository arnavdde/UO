'''
CS 210 Project 3
Author: Arnav De
Credits: lab
Visually present pi using monte carlo's method
'''

import math
import random
import turtle

pie = turtle.Turtle()
pie.speed('fastest')

def draw_circle(pie):
    pie.up()
    pie.goto(0, 200)
    pie.down()
    pie.right(90)
    pie.fd(400)
    pie.up()
    pie.goto(-200, 0)
    pie.down()
    pie.left(90)
    pie.forward(400)
    pie.up()
    pie.goto(-200, 200)
    pie.down()
    pie.forward(400)
    pie.right(90)
    pie.forward(400)
    pie.right(90)
    pie.forward(400)
    pie.right(90)
    pie.fd(400)
    pie.up()
    pie.goto(200, 0)
    pie.down()
    pie.circle(200)


draw_circle(pie)

num_darts = int(input("enter a number of darts: "))

def pi_mc(num_darts):
    random.seed(42) # -> answer to all questions in the universe ;)
    in_circle = 0

    for i in range(num_darts):
        x = random.uniform(-200, 200)
        y = random.uniform(-200,200)

        distance = math.sqrt(x**2 + y**2)

        if distance <= 200:
            in_circle += 1
            pie.up()
            pie.color('blue')
            pie.goto(x, y)
            pie.dot(2)
        else:
            pie.up()
            pie.color('red')
            pie.goto(x, y)
            pie.dot(2)

pi_mc(num_darts)

turtle.exitonclick()