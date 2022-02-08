import csv
file = open("file.csv", "r")
file_csv = csv.reader(file, delimiter=",")
for row in file_csv:
    print(row)
file.close()
