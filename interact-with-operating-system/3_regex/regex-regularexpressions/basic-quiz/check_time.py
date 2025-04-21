#!/usr/bin/env python3
"""
The check_time() function checks for the time format of a 12-hour clock, as follows: the hour is between 1 and 12, with no leading zero, followed by a colon, then minutes between 00 and 59, then an optional space, and then AM or PM, in upper or lower case
"""

import re
def check_time(text):
  pattern = r'^(1[0-2]|[1-9]):([0-5][0-9]) ?([AaPp][Mm])$'
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False
print(check_time("6:02 am")) # True
print(check_time("6:02km")) # False

# Explanation:
# ^ - Start of the string
# (1[0-2]|[1-9]) - Matches the hour part (1-12) with no leading zero
# : - Matches the colon
# ([0-5][0-9]) - Matches the minute part (00-59)
# ? - Matches an optional space
# ([AaPp][Mm]) - Matches AM or PM (case insensitive)
# $ - End of the string
# re.search() - Searches for the pattern in the text