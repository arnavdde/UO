import random
import math
import csv
import matplotlib.pyplot as plt


def load_numerical_data(filename: str, column_titles: list) -> dict:
    """Load data from a CSV file and return a dictionary with keys being the
    row number and values as tuples of the data in each row, converted to float.

    Args:
        filename: The name of the CSV file to load.
        column_titles: A list of columns to load.

    Returns:
        A dictionary where each element corresponds to a data point, with keys 
        corresponding to the row number and values as a tuple of floats.

    Example:
        If column_titles = ['Col1', 'Col3'], and the CSV file has the following data:
            Col1, Col2, Col3
             2.4,  5.6,  7.8
            10.0, 42.5, -3.2
            31.4,  0.5, 12.3
        Then the return dictionary will be:
            {0: (2.4, 7.8), 1: (10, -3.2), 2: (31.4, 12.3)}
    """
    with open(filename, 'r') as r_file:
        reader = csv.reader(r_file, delimiter=',')
        data_dict = {}
        headers = next(reader)

        for column in column_titles:
            col_idx = headers.index(column)
            
            for row_idx, row in enumerate(reader):
                data_dict[row_idx] = tuple(float(row[column]))
    
    return data_dict



def euclid_dist(point1: tuple, point2: tuple) -> float:
    """Compute the Eucledian distance between two points represented as tuples.
    Listing 7.1 in PPC, with modifications for compliance to PEP8

    Args:
        point1: A tuple representing a point in n-dimensional space.
        point2: A tuple representing a point in n-dimensional space.

    Returns:
        float: The Euclidean distance between the two points.

    Example:
        euclid_dist((1, 2.5), (2.1, 4)) should return 1.86 (approximately).
    """
    total = 0
    for index in range(len(point1)):
        diff = (point1[index] - point2[index]) ** 2
        total = total + diff

    euclidDistance = math.sqrt(total)
    return euclidDistance



def create_centroids(k: int, data: dict) -> list:
    """Create k centroids by picking random points from the data until 
    you have k unique centroids.

    Args:
        k: The number of centroids to create.
        data: A dictionary where each element corresponds to a data point, with keys
            corresponding to the row number and values as tuples of floats.

    Returns:
        list: a list of centroids, each centroid is a tuple of floats.
    """
    centroids = []
    centroidCount = 0
    centroidKeys = []

    while centroidCount < k:
        rKey = random.randint(1, len(data))
        if rKey not in centroidKeys:
            centroids.append(data[rKey])
            centroidKeys.append(rKey)
            centroidCount = centroidCount + 1
    
    return centroids


def create_clusters(k: int, centroids: list, data: dict, repeats=100) -> tuple:
    for aPass in range(repeats):
        print("****PASS", aPass + 1, "****")
        clusters = []
        for i in range(k):
            clusters.append([])
        
        for aKey in dada:
            distances = {}
            for clusterIndex in range(K):
                dToC = euclid_dist(data[aKey], centroids[clusterIndex])
                distances.append(dToC)
            
            minDist = min(distances)
            index = distances.index(minDist)

            clusters[index].append(aKey)

        dimensions = len(data[1])
        for clusterIndex in range(k):
            sums = [0] * dimensions
            for aKey in clusters[clusterIndex]:
                dataPoints = data[aKey]
                for ind in range(len(dataPoints)):
                    sums[ind] = sums[ind] + dataPoints[ind]
            for ind in range(len(sums)):
                clusterLen = len(clusters[clusterIndex])
                if clusterLen != 0:
                    sums[ind] = sums[ind] / clusterLen
            
            centroids[clusterIndex] = sums

        for c in clusters:
            print("CLUSTER")
            for key in c:
                print(data[key], end=' ')
            print()
    
    return clusters

def visualize_clusters(dataset_name: str, titles: list, clusters: list,
                       centroids: list) -> plt.Figure:
    """OPTIONAL - Extra credit (up to 50xp)
    Visualize the clusters and centroids. Use a different color for each cluster. 
    Args: 
        dataset_name: The name of the dataset
        titles: list of string column titles
        clusters: list of lists of tuples
        centroids: list of tuples
    Returns:
        matplotlib.pyplot.Figure: The figure object
    """
    pass


def main():
    """ Main driver for the program."""

    # Specifies the files and columns to analyze in the keys, and the number
    # of clusters in the values.
    datasets = {('earthquakes', ('latitude', 'longitude')): 5,
                ('earthquakes', ('depth', 'mag')): 5,
                ('cis210_scores', ('Projects', 'Exams')): 5}
    # Feel free to add more datasets or column pairs and experiment with different values of k

    # Compute clusters for all datasets
    for (dataset, titles), k in datasets.items():
        print(f'\nDataset: {dataset} {titles}')
        # Part 8.1
        data = load_numerical_data(dataset + '.csv', column_titles=titles)

        # Part 8.3
        centroids = create_centroids(k, data)
        print("Initialized the centroids.")

        # Parts 8.2 and 8.4 (create_clusters calls euclid_dist)
        clusters, centroids = create_clusters(k, centroids, data)
        print("\nCreated the clusters.")

        # Optional extra-credit 8.5
        visualize_clusters(dataset, titles, clusters, centroids)
        print("Visualized the clusters.")


if __name__ == '__main__':
    main()