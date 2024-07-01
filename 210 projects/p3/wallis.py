'''
CS 210 Project 3
Author: Arnav De
Credits: lab
Compute pi using wallis's method
'''

import math

num_pairs = int(input("enter a number of pairs: "))

def pi_wallis(num_pairs):
    acc = 1
    num = 2
    for pair in range(num_pairs):
        left_term = num / (num - 1)
        right_term = num / (num + 1)
        acc = acc * left_term * right_term
        num += 2
    
    wallis_pi = acc * 2
    print("pi is approximately: " + str(wallis_pi))

    return wallis_pi

pi_wallis(num_pairs)