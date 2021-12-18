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
    actionList = list (input().split)
    # read helloworld.exe
        # if read - check read is in permission list of the dictionary
    if actionList[1] == "Read" and "R" in dictionary1[actionList[0]]:
        print ("OK")
    else:
        print("Access Denied")
    if actionList[1] == "Write" and "W" in dictionary1[actionList[0]]:
        print ("OK")
    else:
        print("Access Denied")
    if actionList[1] == "Execute" and "X" in dictionary1[actionList[0]]:
        print ("OK")
    else:
        print("Access Denied")