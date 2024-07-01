import json
import statistics as stat

# import pandas


def filter_arr(an_arr, low_lim=0):
    # your implementation goes here
    pass
    

def read_data(file_name, keys):
    # your implementation goes here
    f = open(file_name)
    data = json.load(f)
    #iterate thru json, iterate thru dicts in json, if key in dict, append dict[key] to a list
    return_list = []
    for key in keys:
        return_list.append([])
    for dict in data:
        for key in range(len(keys)):
            return_list[key].append(dict[keys[key]])
    return return_list


        
def stats(an_array):
    # replace the ellipsis with your implementation of each of the statistics    
    stats_dict = {
        'min': min(an_array), 
        'max': max(an_array), 
        'range': max(an_array) - min(an_array),
        'mean': round(stat.mean(an_array), 2), 
        'mode': round(stat.mode(an_array), 2),
        'var': round(stat.variance(an_array), 2), 
        'stdev': round(stat.stdev(an_array, 2)),
    }
    return stats_dict

# your may implement any other auxiliary functions

def print_stats(file_name):
# your implementation goes here
    data_list = read_data(file_name, ['pop2023', 'growth', 'density'])
    
    for pop23 in data_list[0]:
        if pop23 < 10000:
            data_list[1].pop(data_list[0].index(pop23))
            data_list[2].pop(data_list[0].index(pop23))
            data_list[0].pop(data_list[0].index(pop23))

    pop_dict = stats(data_list[0])
    growth_dict = stats(data_list[1])
    density_dict = stats(data_list[2])

    print(f"""
                      +-------------+-------------+-------------+-------------+-------------+-------------+-------------+
                      |min          |max          |range        |mean         |mode         |variance     |st.dev.      |
                      +-------------+-------------+-------------+-------------+-------------+-------------+-------------+
          population  |{str(pop_dict['min']).ljust(13)}|{str(pop_dict['max']).ljust(13)}|{str(pop_dict['range']).ljust(13)}|{str(pop_dict['mean']).ljust(13)}|{str(pop_dict['mode']).ljust(13)}|{str(pop_dict['var']).ljust(13)}|{str(pop_dict['stdev']).ljust(13)}|
                      +-------------+-------------+-------------+-------------+-------------+-------------+-------------+
          growth      |{str(growth_dict['min']).ljust(13)}|{str(growth_dict['max']).ljust(13)}|{str(growth_dict['range']).ljust(13)}|{str(growth_dict['mean']).ljust(13)}|{str(growth_dict['mode']).ljust(13)}|{str(growth_dict['var']).ljust(13)}|{str(growth_dict['stdev']).ljust(13)}|
                      +-------------+-------------+-------------+-------------+-------------+-------------+-------------+
          density     |{str(density_dict['min']).ljust(13)}|{str(density_dict['max']).ljust(13)}|{str(density_dict['range']).ljust(13)}|{str(density_dict['mean']).ljust(13)}|{str(density_dict['mode']).ljust(13)}|{str(density_dict['var']).ljust(13)}|{str(density_dict['stdev']).ljust(13)}|
                      +-------------+-------------+-------------+-------------+-------------+-------------+-------------+
          """)



    

if __name__ == "__main__":
    print_stats('population.json')