#!/usr/bin/env python3

import re
# Wildcards . *
# Character classes [ ], range: - (dash_)
print(re.search(r"[a-z]way", "The end of the highway"))

str1 = "The end of the highway"
regex1 = r"[a-z]way"
print(re.search(regex1,str1)) # <re.Match object; span=(18, 22), match='hway'>

str1 = "What a way to go"
regex1 = r"[a-z]way"
print(re.search(regex1,str1)) # None


print(re.search(r"cloud[a-zA-Z0-9]", "cloudy")) # <re.Match object; span=(0, 6), match='cloudy'>
print(re.search(r"cloud[a-zA-Z0-9]", "cloud9")) # <re.Match object; span=(0, 6), match='cloud9'>
