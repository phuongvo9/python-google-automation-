#!/usr/bin/env python3
import os

# remove file

os.remove ("novel.txt")

#rename a file

os.rename ("spider.txt", "spider_rename.txt")
os.rename ("spider_rename.txt", "spider.txt")

# OS path sub-modules'exists check if a file exists
print (os.path.exists("spider_rename.txt"))

#Getsize checks file size and returns in bytes

print(os.path.getsize("spider.txt"))

#getmtime checks last modified and returns Unix timestamp

print (os.path.getmtime("spider.txt"))
