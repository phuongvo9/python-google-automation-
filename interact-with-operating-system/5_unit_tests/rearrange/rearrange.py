#!/usr/bin/env python3

import re
"""
This function rearranges a name from "Last, First" format to "First Last" format
"""

def rearrange_name(name):
  result = re.search(r"^([\w .]*), ([\w .]*)$", name)
  return "{} {}".format(result[2], result[1])