import json
import matplotlib.pyplot as plt
# place additional imports here

def plot_pop_data(pop, lat, lon):
    # your implementation goes here
    pass

def plot_hist(data, n_bins=10):
    # your implementation goes here
    pass

if __name__ == "__main__":
    file_name = "population.json"
    
    [pop, lat, lon, growth, dens] = read_data(file_name, \
        ["pop2023", "lat", "lng", "growth", "density"])
    
    plot_pop_data(pop, lat, lon)
    
    pop = filter_arr(pop, 10000)

    plot_hist(dens)