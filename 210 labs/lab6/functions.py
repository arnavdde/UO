'''
CS 210 Project 6
Author: Arnav De
Credits: 
Goals: text file IO, matplotlib, list and dict comprehension

'''

import json
import statistics
import matplotlib

def read_data(file_name: str) -> list:
    with open(file_name, 'r') as read_file:
        split_file = [line.split(',') for line in read_file]
    return split_file

def list_to_dict(a_list: list) -> dict:
    data_dict = {int(index[0][:4]): float(index[1]) for index in a_list}
    return data_dict

def dict_to_list(a_dict: dict) -> list:
    data_list = [[year, rainfall] for year, rainfall in a_dict.items()]
    return data_list

def mean_rainfall(values: list) -> float:
    i = 0
    avg_rain = 0
    for year, rainfall in values:
        counter = rainfall 
        avg_rain += counter
        i += 1
    return avg_rain / i

def high_rain_years(file_name):
    pass
    # with open(file_name, 'r') as read_file:
    #     split_file = [line.split(',') for line in read_file]
        
