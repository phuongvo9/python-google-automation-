"""READING CSV FILES"""

import csv

f = open ("csv/csv_file.txt")

#parases the file using the CSV module

csv_f = csv.reader(f)
for row in csv_f:
    #unpack value from the file
    name, phone, role = row
    print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))

f.close()

# Output:
    # Name: Sabrina Green, Phone: 802-867-5309, Role: System Admin
    # Name: Eli Jones, Phone: 684-348-1127, Role: IT Specialist


"""Reading and Writing CSV files with DICTIONARIES"""

# DictReader turns each row of the data in a CSV file into a dictionary

with open ("csv/software.csv") as software:
    reader = csv.DictReader(software)
    for row in reader:
        