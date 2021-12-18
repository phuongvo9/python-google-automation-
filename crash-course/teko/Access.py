#!/usr/bin/env python3
"""
Teko Test: Access Right 18/12/2021
"""


n = int(input())
com = {}
for i in range(n):
    myList = list(input().split())
    com[myList[0]] = myList[1:len(myList)]


m = int(input())
for t in range(m):
    opps = list(input().split())
    if 'W' in com[opps[1]] and opps[0] == 'write':
        print('OK')
    elif 'R' in com[opps[1]] and opps[0] == 'read':
        print('OK')
    elif 'X' in com[opps[1]] and opps[0] == 'execute':
        print('OK')
    else:
        print('Access denied')

    
#####

#  N — the number of files contained in the filesystem
n = int (intput())

# Empty dictionary - # Use dictionary to store <filename> <Read Write Execute>
dictionary1 = {}
for i in range(n):
    #create a list to store input value: <filename> <Read Write Execute>
    inputList = list (input().split())
    # Use dictionary key = <filename> _ value: <Read Write Execute>
    dictionary1[inputList[0]] = inputList[1:len(inputList)]
