import matplotlib.pyplot as plt
import csv

def read_data(file_name):
    # #your implementation goes here
    # with open(file_name, 'r') as f:
    #     row_reader = csv.reader(f)
    #     fields = next(row_reader)

    #     row_list = [line for line in row_reader]

    #     city_dict = {}

    #     for row in row_list:
    #         city_key = {row[0], row[1]}

    #         city_indices = {}

    #         for i in range(3, len(fields)):
    #             city_indices[fields[i]] = row[i]
            
    #         city_dict[city_key] = city_indices

    # return city_dict
    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        fields = next(reader)
        outer_dict = {}

        for line in reader:
            key = (line[0], line[1])
            inner_dict = {}
            for i in range(3, len(fields)):
                inner_dict[fields[i]] = line[i]
            outer_dict[key] = inner_dict

        return outer_dict

def create_total_score(data_dict):
    for city_dict in data_dict.values():
        total = 0
        for field in city_dict.values():
            total += float(field)
    city_dict['total_score'] = total

# define auxiliary functions here
def extract_column(data_dict, col_name):
    column = []
    for city_dict in data_dict.values():
        column += [float(city_dict[col_name])]
        return column
            
def plot_data(data_dict):
    x = extract_column(data_dict, 'Housing')
    y = extract_column(data_dict, 'Cost_of_Living')

    plt.figure(figsize = (16,8))
    plt.scatter(x, y, marker='x', c='green')
    plt.title('Housing vs Cost of Living')
    plt.xlabel('housing')
    plt.ylabel('cost of living')
    plt.savefig(f'scatter_H_C.png')
    plt.show()

if __name__ == "__main__":
    housing_dict = read_data('city_scores.csv')
    print(extract_column(housing_dict, 'Housing'))
    plot_data(housing_dict)