#!/usr/bin/env python3
"""
Teko Test: Access - Test #2 18/12/2021
Sample test:
    4
    helloworld.exe R X
    pinglog W R
    nya R
    goodluck X W R
    5
    read nya
    write helloworld.exe
    execute nya
    read pinglog
    write pinglog

"""


#  N — the number of files contained in the filesystem
n = int(input())

# Empty dictionary - # Use dictionary to store <filename> <Read Write Execute>
dictionary1 = {}
for i in range(n):
    #create a list to store input value: <filename> <Read Write Execute>
    inputList = list (input().split())
    # Use dictionary key = <filename> _ value: <Read Write Execute>
    dictionary1[inputList[0]] = inputList[1:len(inputList)]
        
#input: sample input1
#print (dictionary1)
#{'helloworld.exe': ['R', 'X'], 'pinglog': ['W', 'R'], 'nya': ['R'], 'goodluck': ['X', 'W', 'R']}


m = int(input())
for j in range (m):
    #create a list to store input value <Action R|W|E> <Filename>
    actionList = list(input().split())
    # read helloworld.exe
        # if read - check read is in permission list of the dictionary
    if actionList[0] == "read" and "R" in dictionary1[actionList[1]]:
        print ("OK")
    elif actionList[0] == "write" and "W" in dictionary1[actionList[1]]:
        print ("OK")
    elif actionList[0] == "execute" and "X" in dictionary1[actionList[1]]:
        print ("OK")
    else:
        print("Access denied")