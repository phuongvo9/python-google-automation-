#!/usr/bin/env python3

import re
"""
This function rearranges a name from "Last, First" format to "First Last" format
"""
# UnboundLocalError: cannot access local variable 'result' where it is not associated with a value
def rearrange_name(name):
  result = re.search(r"^([\w .]*), ([\w .]*)$", name)
  if result is None:
    return name

  return "{} {}".format(result[2], result[1])