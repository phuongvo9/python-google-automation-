n = int(input())

for i in range(n):
    originalList = list (int(input()))

result = []
for i in range (len(originalList)):
    count = 0
    for j in range (len(originalList)):
        if originalList[i] > originalList [j]:
            count +=1
    
    result.append(count)

print (result)
