# Reading and Writing files
# Creates a new file object and assigning it to a variable called file

file = open ("using-python-to-interact-with-the-operating-system/week-two/spider.txt")

# readline method reads a single line of a file
print(file.readline())

# readline method reads the second line of a file - each time the readline method isi called the file object updates current position in the file)
print (file.readline())

print(file.read())

file.close

