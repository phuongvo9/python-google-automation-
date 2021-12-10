#!/usr/bin/env python3

# Reading and Writing files
# Creates a new file object and assigning it to a variable called file

file = open ("spider.txt")

# readline method reads a single line of a file
print(file.readline())

# readline method reads the second line of a file - each time the readline method isi called the file object updates current position in the file)
print (file.readline())

print(file.read())
# We have to close opened file
file.close


#############  WITH OPEN _ FILE ################333

"""With keyword creates block of code with the work needs to be done with the file inside"""

"""When 'with' is used. Python will automatically close the file"""

with open("spider.txt") as file:
    print (file.readline())

with open ("spider.txt") as file:
    print (file.readline())

with open ("spider.txt") as file:
    for line in file:
        print(line.upper())


# Empty lines can be avoided by using STRIP

with open ("spider.txt") as file:
    for line in file:
        print (line.strip().upper())


