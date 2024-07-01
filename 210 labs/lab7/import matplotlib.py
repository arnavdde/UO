import matplotlib.pyplot as plt
import csv

def read_data(file_name):
    #your implementation goes here
    with open(file_name, 'r') as f:
        row_reader = csv.reader(f)
        fields = next(row_reader)

        row_list = [line for line in row_reader]

        city_dict = {}

        for row in row_list:
            city_key = {row[0], row[1]}

            city_indices = {}

            for i in range(3, len(fields)):
                city_indices[fields[i]] = row[i]
            
            city_dict[city_key] = city_indices

    return city_dict

def create_total_score(data_dict):
    # your implementation goes here

# define auxiliary functions here
            
def plot_data(data_dict):
    # your implementation goes here

if __name__ == "__main__":
    # the main conditional execution