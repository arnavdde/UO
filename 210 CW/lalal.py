import csv 







def load_numerical_data(filename: str, column_titles: list) -> dict:
    with open(filename, 'r') as r_file:
        reader = csv.reader(r_file, delimiter=',')
        data_dict = {}
        headers = next(reader)

        col_index = [headers.index(col) for col in column_titles]
        
        row_index = 0 
        for row in reader:
            try:
                selected_data = [float(row[idx]) for idx in col_index]
                if len(selected_data) == len(column_titles):
                    data_dict[row_index] = tuple(selected_data)
                    row_index += 1  
            except ValueError:
                continue

    return data_dict



def create_clusters(k: int, centroids: list, data: dict, repeats=100) -> tuple:
    for aPass in range(repeats):
        clusters = []
        for i in range(k):
            clusters.append([])
        for aKey in data:
            distances = []
            for clusterIndex in range(k):
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

    for aKey in range(len(clusters)):
        for anIndex in range(len(clusters[aKey])):
            clusters[aKey][anIndex] = data[clusters[aKey][anIndex]]
    
    return clusters, centroids