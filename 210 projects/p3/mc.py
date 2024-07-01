'''
CS 210 Project 3
Author: Arnav De
Credits: lab
Compute pi using monte carlo's method
'''

import math
import random

num_darts = int(input("enter a number of darts: "))

def pi_mc(num_darts):
    random.seed(42) # -> answer to all questions in the universe ;)
    in_circle = 0

    for i in range(num_darts):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2 + y**2)

        if distance <= 1:
            in_circle += 1
    
    mc_pi = in_circle / num_darts * 4
    print(" pi is approximately: " + str(mc_pi))

    return mc_pi

pi_mc(num_darts)
