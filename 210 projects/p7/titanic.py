import titanic
import matplotlib.pyplot as plt
import statistics
import csv
from collections import Counter
# Write your functions here

def load_data(file_name:str, types:dict) -> dict:
    with open(file_name, 'r') as titanicfile:
        reader = csv.reader(titanicfile, delimiter=',')
        data_dict = {}
        headers = next(reader)

        for column, data_type in types.items():
            column_key = (column, data_type)
            data_dict[column_key] = []
            column_index = headers.index(column)

            for row in reader:
                data_dict[column_key].append(data_type(row[column_index]))

            titanicfile.seek(0)
            next(reader)  

    return data_dict
        
def summarize(data: dict):
    specific_word = 7
    specific_value = 6

    for(column_name, _), values in data.items():
        print(f"Statistics for {column_name}:")

        if isinstance(values[0], (int, float)):
            min_val = min(values)
            max_val = max(values)
            mean_val = statistics.mean(values)
            stdev_val = statistics.stdev(values)
            mode_val = statistics.mode(values)

            print(f"{'min':>{specific_word}}: {min_val:>{specific_value}.1f}")
            print(f"{'max':>{specific_word}}: {max_val:>{specific_value}.1f}")
            print(f"{'mean':>{specific_word}}: {mean_val:>{specific_value}.1f}")
            print(f"{'stdev':>{specific_word}}: {stdev_val:>{specific_value}.1f}")

            if isinstance(mode_val, (int, float)):
                mode = f"{mode_val:.1f}"
            else:
                mode = mode_val[0]
            print(f"{'mode':>{specific_word}}: {mode:>{specific_value}.1f}")
        else:
            unique_str = set(values)
            num_unique_str = len(unique_str)
            print(f"{'Number of unique strings':>{specific_word}}: {num_unique_str}")

            counter = Counter(values)
            mode_val = counter.most_common(1)[0][0]
            print(f"{'       Most common value'}: {mode_val}")

def pearson_corr(x: list, y: list) -> float:
    if type(x[0]) not in [int, float] or type(y[0]) not in [int, float]:
        raise ValueError("pearson_corr only works with int or float lists.")
    elif len(x) != len(y):
        raise ValueError("The list parameters must have the same number of elements.")
    else:
        x_bar = statistics.mean(x)
        y_bar = statistics.mean(y)
        x_stdev = statistics.stdev(x)
        y_stdev = statistics.stdev(y)
        num = 0.0
        for i in range(len(x)):
            num = num + (x[i] - x_bar) * (y[i] - y_bar)
        corr = num / ((len(x) - 1) * x_stdev * y_stdev)
        return round(corr, 2)

def survivor_vis(data: dict, col_1:tuple, col_2:tuple) -> plt.figure:
    survivor_list = data[('Survived', int)]
    col_list1 = data[col_1]
    col_list2 = data[col_2]
    survivor_col1 = []
    survivor_col2 = []
    casualty_col1 = []
    casualty_col2 = []

    for i in range(len(survivor_list)):
        if survivor_list[i] == 1:
            survivor_col1.append(col_list1[i])
            survivor_col2.append(col_list2[i])
        else:
            casualty_col1.append(col_list1[i])
            casualty_col2.append(col_list2[i])

    plt.scatter(survivor_col1, survivor_col2, c='green', marker = '*', label = 'Survived')
    plt.scatter(casualty_col1, casualty_col2, c='red', marker = 'x', label = 'Died')
    plt.xlabel(col_1[0])
    plt.ylabel(col_2[0])
    plt.title("Survival of Titanic Passengers")
    plt.legend()
    plt.show()

# ------ You shouldn't have to modify main --------
def main():
    """Main program driver for Project 3."""

    # 3.1 Load the dataset
    titanic_types = {'PassengerId': int, 'Survived': int, 'Pclass': int,
                     'Sex': str, 'Age': float, 'SibSp': int, 'Parch': int,
                     'Fare': float, 'Embarked': str, 'FamilySize': int,
                     'age_group': str}
    data = load_data('titanic_clean.csv', titanic_types)

    # 3.2 Print informative summaries
    print("\nPart 3.2")
    summarize(data)

    print("\nPart 3.3")
    # 3.3 Compute correlations between age and survival
    corr_age_survived = pearson_corr(data[('Age', float)],
                                     data[('Survived', int)])
    print(f'Correlation between age and survival is {corr_age_survived:3.2f}')

    # 3.3 Correlation between fare and survival
    corr_fare_survived = pearson_corr(data[('Fare', float)],
                                      data[('Survived', int)])
    print(f'Correlation between fare and survival is {corr_fare_survived:3.2f}')

    # 3.3 Correlation between family size and survival
    corr_fare_survived = pearson_corr(data[('FamilySize', int)],
                                      data[('Survived', int)])
    print(f'Correlation between family size and survival is'
          f' {corr_fare_survived:3.2f}')

    # 3.4 Visualize results
    fig = survivor_vis(data, ('Age', float), ('Fare', float))
    fig = survivor_vis(data, ('Age', float), ('Pclass', int))
    fig = survivor_vis(data, ('Age', float), ('Parch', int))


if __name__ == "__main__":
    main()
