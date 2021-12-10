import os
import datetime

# convert the Unix timestamp
timestamp = os.path.getmtime ("spider.txt")
print (datetime.datetime.fromtimestamp(timestamp))

# absolute path function 

print (os.path.abspath("spider.txt"))

"""Directories"""

#getcwd checks which current directory

print(os.getcwd())

#mkdir function creates a directory

os.mkdir ("new_dir")

# chdir function swtiches to another directory

os.chdir ("new_dir")

print (os.getcwd())

os.chdir("..")

# rmdir fucntion removes a directory
os.rmdir(os.path.abspath("new_dir"))

os.chdir("..")

# listdir returns a LIST of all files and sub-dir

print(os.listdir("week-two"))

dir = "week-two"
os.mkdir ("week-two/another_new_dir")

for name in os.listdir(dir):
    #os .path.join creatse full path and can be used to check if file/directory"
    fullname = os.path.join(dir,name)
    if os.path.isdir(fullname):
        print ("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))
os.rmdir ("week-two/another_new_dir")

