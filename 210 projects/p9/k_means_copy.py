import random
import math
import csv
import matplotlib.pyplot as plt


def load_numerical_data(filename: str, column_titles: list) -> dict:
    data_dict = {}
    with open(filename, 'r') as readfile:
        reader = csv.DictReader(readfile)
        counter = 0
        for row in reader:
            try:
                data_dict[counter] = tuple(float(row[column]) for column in column_titles)
                counter += 1
            except ValueError:
                continue
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
    pass


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
    pass


def create_clusters(k: int, centroids: list, data: dict, repeats=100) -> tuple:
    for aPass in range (repeats):
        print("****PASS", aPass+ 1, "****")
        clusters = []
        for i in range (k):
            clusters.append([])
        
        for aKey in data: #calculate distance to centroid
            distances = []
            for clusterIndex in range (k):
                dToC = euclid_dist (data[aKey], centroids[clusterIndex]) 
                distances.append(dToC)

            minDist = min (distances) #find minimum distance 
            index= distances.index(minDist)

            clusters [index].append(aKey) #add to cluster

        dimensions = len(dataDict [1]) #recompute the clusters 
        for clusterIndex in range (k):
            sums = [0] * dimensions
            for aKey in clusters [clusterIndex] :
                dataPoints = data[aKey]
                for ind in range(len(dataPoints)): #calculate sums 
                    sums [ind] = sums [ind] + dataPoints [ind] #calculate average
            for ind in range (len (sums) ):
                clusterLen = len(clusters [clusterIndex])
                if clusterLen != 0:
                    sums [ind] = sums [ind]
            
            centroids [clusterIndex] = sums #assign avg to centroids
        
        for c in clusters:
            print ("CLUSTER")
            for key in c:
                print (data[key], end = " ")
            print ()
    
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