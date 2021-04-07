import csv

def write_to_csv(Data_to_write, filename):
    with open(filename, 'w', encoding='utf-8', newline='\n') as csvfile:
        csvwriter = csv.writer(csvfile)
        for p in Data_to_write:
            csvwriter.writerow(p)

def read_xyz_from_csv(filename):
    with open(filename, encoding='utf-8', newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for x,y,z in reader:
            yield (float(x), float(y), float(z))