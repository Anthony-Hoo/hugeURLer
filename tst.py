import csv

with open('./redirectionConfig.csv', 'r') as f:
        data = list(csv.reader(f))
        del(data[0])
        print(data)