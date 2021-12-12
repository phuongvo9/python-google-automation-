#!/usr/bin/env python3


#find the runner-up score. The first line contains . The second line contains an array   of  integers each separated by a space
#Sample input:
# 5
# 2 3 6 6 5

if __name__ == '__main__':
    n = int(input())
    arr = map(int,input().split())

scores = list(arr)

# Find winner
winner = 0
for i in scores:
    if i > winner:
        winner = i

#winner = max(scores)
low_scores = []
for item in scores:
    if item < winner:
        low_scores.append(item)

runner_up = max(low_scores)
print (str(runner_up))






