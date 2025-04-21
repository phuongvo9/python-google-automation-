#!/usr/bin/env python3
"""
The contains_acronym() function checks the text for the presence of 2 or more characters or digits surrounded by parentheses, with at least the first character in uppercase (if it's a letter), returning True if the condition is met, or False otherwise. For example, "Instant messaging (IM) is a set of communication technologies used for text-based communication" should return True since (IM) satisfies the match conditions.
"""

import re
def contains_acronym(text):
  pattern = r"\([A-Z0-9]{1}[a-zA-Z0-9]+\)"
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True


# Explanation:
# \(: Matches an opening parenthesis ( literally
# [A-Z0-9]{1}: Matches exactly one character that is either an uppercase letter (A-Z) or a digit (0-9). This ensures that the first character inside the parentheses is either an uppercase letter or a digit
# [a-zA-Z0-9]+: Matches one or more alphanumeric characters (lowercase letters a-z, uppercase letters A-Z, or digits 0-9) that follow the first character
# \): Matches a closing parenthesis ) literally
