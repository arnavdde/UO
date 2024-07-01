import csv

def readtodict(file_name):
    
    with open(file_name, 'r') as read_file:
        csv_reader = csv.reader(read_file)
        
        data_dict = {row[0]: row[1].strip() for row in csv_reader}

    print(data_dict)

if '__name__' == '__main__':
    res_dict = readtodict("rainfall.csv")
    readtodict(res_dict)