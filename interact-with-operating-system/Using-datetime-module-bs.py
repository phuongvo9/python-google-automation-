import os
import datetime

# convert the Unix timestamp
timestamp = os.path.getmtime ("spider.txt")
print (datetime.datetime.fromtimestamp(timestamp))

# absolute path function 

print (os.path.abspath("spider.txt"))

