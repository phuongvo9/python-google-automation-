"""READING CSV FILES"""

import csv
import os
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


"""Reading CSV files with DICTIONARIES"""

# DictReader turns each row of the data in a CSV file into a dictionary

with open ("csv/software.csv") as software:
    reader = csv.DictReader(software)
    for row in reader:
        print("{} has {} users".format(row["name"],row["users"]))



"""Writing to CSV files with DICTIONARIES"""
# DictWriter generates a CSV file from contents of a LIST of Dictionaries

users = [
    {"name":"Phuong Huy Vo", "username":"phuongvo9","department":"IT Site Reliability Engineering"},
    {"name": "Jack Vo","username":"j.vo", "department":"IT infrastructure"},
    {"name": "Tsu Qwan","username":"t.qwan", "department":"IT Development"}
]

keys = ["name","username","department"]

with open ("csv/by_department.csv", "w") as by_department:
    writer = csv.DictWriter (by_department, fieldnames= keys)
    writer.writeheader()
    writer.writerows(users)

os.remove ("csv/by_department.csv")