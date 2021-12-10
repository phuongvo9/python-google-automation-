#!/usr/bin/env python3
import os

# remove file

os.remove ("novel.txt")

#rename a file

os.rename ("spider.txt", "spider_rename.txt")
os.rename ("spider_rename.txt", "spider.txt")

# OS path sub-modules'exists check if a file exists
print (os.path.exists("spider_rename.txt"))

