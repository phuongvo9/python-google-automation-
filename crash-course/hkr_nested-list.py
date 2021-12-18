#!/usr/bin/env python3

"""
Given the names and grades for each student in a class of  students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Ref: https://www.programiz.com/python-programming/list-comprehension
"""

if __name__ == '__main__':
    records = []
    for i in range (int(input())):
        name = input()
        score = float(input())

        #input records
        records.append([name,score])
    
    print (records)