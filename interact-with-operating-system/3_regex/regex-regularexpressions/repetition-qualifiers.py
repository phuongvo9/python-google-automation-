#!/usr/bin/env python3

import re

# Search for a sequence of exactly 5 alphabetic characters (uppercase or lowercase)
print(re.search(r"[a-zA-Z]{5}", "a ghost"))  # Matches "ghost" (5 alphabetic characters)

# Search for the first sequence of exactly 5 alphabetic characters in the string
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))  # Matches "scary" (first match)

# Find all sequences of exactly 5 alphabetic characters in the string
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))  # Matches ["scary", "ghost"]

# Search for a sequence of exactly 3 digits
print(re.search(r"\d{3}", "My number is 123456"))  # Matches "123" (first 3 digits)

# Find all whole words (bounded by word boundaries) that are exactly 5 alphabetic characters long
print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared"))  # Matches ["scary", "ghost"]

# Find all sequences of alphanumeric characters (letters, digits, or underscores) 
# that are between 5 and 10 characters long
print(re.findall(r"\w{5,10}", "I really like strawberries"))  # Matches ["really", "strawberri"]

# Find all sequences of alphanumeric characters that are at least 5 characters long
print(re.findall(r"\w{5,}", "I really like strawberries"))  # Matches ["really", "strawberries"]

# Search for a sequence starting with "s" followed by up to 20 alphanumeric characters
print(re.search(r"s\w{,20}", "I really like strawberries"))  # Matches "strawberries"