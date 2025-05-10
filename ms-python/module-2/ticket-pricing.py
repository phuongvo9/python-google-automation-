#!/usr/bin/env python3

"""
This program calculates the price of a movie ticket based on the age of the customer.
instead of printing the price category, 
we need the program to output the actual price.  
For example, if the input age is 10, the output should be 8, not "Children are $8."
 How would you modify your code to output the numerical price?
"""

age = int(input("How old are you? "))

if age < 12:
    print(8)
elif age >= 12 and age <= 64:
    print(12)
else:
    print(10)
"""
store the calculated price in a variable for further use, such as calculating total revenue or applying discounts. How would you modify your code to store the price in a variable called "ticket_price" and then print the value of that variable?
"""

age = int(input("How old are you? "))

if age < 12:
    ticket_price = 8
elif age >= 12 and age <= 64:
    ticket_price = 12
else:
    ticket_price = 10

print(ticket_price)
