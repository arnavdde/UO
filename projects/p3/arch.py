'''
CS 210 Project 3
Author: Arnav De
Credits: lab
Compute Pi using Archimedes's method
'''

import math

num_sides = int(input("enter a number of sides: "))

def pi_arch(num_sides):
    
    inner_angle_b = 360.0 / num_sides
    half_angle_a = inner_angle_b / 2
    one_half_sides_s = math.sin(math.radians(half_angle_a))
    side_s = one_half_sides_s * 2
    polygon_circumference = num_sides * side_s
    arch_pi = polygon_circumference / 2
    print("Pi is approximately: " + str(arch_pi))
    return arch_pi

pi_arch(num_sides)

