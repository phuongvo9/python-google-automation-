"""
The function sum_positive_numbers should return the sum of all positive numbers between the number n received and 1. 
For example, when n is 3 it should return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15. Let's make this work
"""
# Remeber to define Base case!

def sum_positive_numbers(n):
    #The base case is n being smaller than 1
    if n < 1:
        return n
    
    # The recursive case is adding this number to sum of the numbers smaller than this one
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(9))

