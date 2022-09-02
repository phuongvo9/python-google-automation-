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


"""
    The "r" at the beginning of the pattern indicates that this is a rawstring
    Always use rawstrings for regular expressions in Python
    \d to match digits
    +, plus character, to match one or more occurrences
    [ ] square brackets [] - character classes
"""


regex = r"\[(\d+)\]"
result = re.search (regex, log)
# result is a re.match object

print (result[0]) #Output: [411601]
print (result[1]) #Output: 411601

##### --------------------------------------------------------------------------

result = re.search(r'aza', 'bazaar')
print (result) #output:  <re.Match object; span=(1, 4), match='aza'>

# None is a special value that there's none actual value there - None for no returns
result = re.search (r'aza','maze')
print(result) #output: None

print(re.search (r"%x","xenon"))    # None
print(re.search(r"p.ng","penguin")) # <re.Match object; span=(0, 4), match='peng'>
print(re.search(r"p.ng", "sponge")) # <re.Match object; span=(1, 5), match='pong'>

# search function can be added as a third parameter
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE)) # <re.Match object; span=(0, 4), match='Pang'>
print(re.search(r"p.ng", "Pangaea2s", re.IGNORECASE)) # <re.Match object; span=(0, 4), match='Pang'>
print(re.search((r"w*com"),"www.facebook.com")) #<re.Match object; span=(13, 16), match='com'>





