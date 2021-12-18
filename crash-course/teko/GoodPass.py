#!/usr/bin/env python3
"""
Teko Interview: Good password
Using regular expression search in re module
"""
import re

def isGoodpassword (yourpass):
    """
    Check password with if else blocks
    """
    reg = "^(?=.*[a-z])(.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,16}$"
    # compiling regex
    pattern = re.compile(reg)
    is_match = re.search(pattern, yourpass)

    # Length is not valid
    if len(yourpass) < 6 or len(yourpass) > 16:
        return False
    elif not is_match:
        return False
    # not have any character in [a-z] - use rawstring from coursera

    # elif not re.search (r"[a-z]", yourpass):
    #     return False
    # # not have any character in [A-Z]
    # elif not re.search (r"[A-Z]", yourpass):
    #     return False
    # # not have any character in [0-9]
    # elif not re.search (r"[0-9]", yourpass):
    #     return False
    
    # elif not re.search (r"[$#@]", yourpass):
    #     return False

    return True


if __name__ == '__main__':
    yourpass = input()
    if isGoodpassword(yourpass):
        print ("YES")
    else:
        print ("NO")