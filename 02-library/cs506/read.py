import csv

def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    with open(csv_file_path) as csvfile:
        csvread = csv.reader(csvfile)
        ret = []
        for row in csvread:
            for i in range(len(row)):
                if row[i].isdigit():
                    row[i] = int(row[i])
            ret.append(row)

    return ret
