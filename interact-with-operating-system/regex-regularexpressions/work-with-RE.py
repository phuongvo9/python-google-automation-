#!/usr/bin/env python3

log = "July 31 7:51:48 mycomputer bad_process[411601]: ERROR Perfroming package upgrade"
    #Get index of [ in string 
index = log.index('[')

# Hard way to extract numbers by using Index from string
print (log[index+1:index+7])
#output: 411601

# Can we find the better way?

# re module allows us find regular expressions inside strings
import re

log = "July 31 7:51:48 mycomputer bad_process[411601]: ERROR Perfroming package upgrade"

#  \d to match digits
# +, plus character, to match one or more occurrences
# [ ] square brackets [] - character classes

regex = r"\[(\d+)\]"
result = re.search (regex, log)
# result is a re.match object

print (result[0]) #Output: [411601]
print (result[1]) #Output: 411601

