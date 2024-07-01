'''
CS 210 Project 3
Author: Arnav De
Credits: lab
Compute the number of iterations needed by each method
to comply with a chosen input error tolerance. 
'''

import math
import random




def pi_arch(num_sides):
    inner_angle_b = 360.0 / num_sides
    half_angle_a = inner_angle_b / 2
    one_half_sides_s = math.sin(math.radians(half_angle_a))
    side_s = one_half_sides_s * 2
    polygon_circumference = num_sides * side_s
    arch_pi = polygon_circumference / 2
    return arch_pi

def pi_wallis(num_pairs):
    acc = 1
    num = 2
    for pair in range(num_pairs):
        left_term = num / (num - 1)
        right_term = num / (num + 1)
        acc = acc * left_term * right_term
        num += 2
    
    wallis_pi = acc * 2
    return wallis_pi

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

    return mc_pi

def all_pi(err_tol):
    num_sides = 1
    while abs(math.pi - pi_arch(num_sides)) >= err_tol:
        num_sides += 1
    
    arch_pi_final = pi_arch(num_sides)
    print(f"Archimedes: num_sides = {num_sides} (Differs by {round(abs(math.pi - arch_pi_final), 19)})")

    num_pairs = 1
    while abs(math.pi - pi_wallis(num_pairs)) >= err_tol:
        num_pairs +=1
    
    wallis_pi_final = pi_wallis(num_pairs)
    print(f"Wallis: num_pairs = {num_pairs} (Differs by {round(abs(math.pi - wallis_pi_final), 19)})")


    num_darts = 1
    while abs(math.pi - pi_mc(num_darts)) >= err_tol:
        num_darts +=1

    mc_pi_final = pi_mc(num_darts)
    print(f"Monte Carlo: num_darts = {num_darts} (Differs by {round(abs(math.pi - mc_pi_final), 19)})")
    list = []
    list.append(num_sides)
    list.append(num_pairs)
    list.append(num_darts)
    return list


all_pi(0.1)