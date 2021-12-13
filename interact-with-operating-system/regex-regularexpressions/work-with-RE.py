#!/usr/bin/env python3

log = "July 31 7:51:48 mycomputer bad_process[411601]: ERROR Perfroming package upgrade"
    #Get index of [ in string 
index = log.index('[')

# Hard way to extract numbers by using Idex from string
print (log[index+1:index+6])
#output: 411601

# Can we find the better way?

# re module allows us find regular expressions inside strings


