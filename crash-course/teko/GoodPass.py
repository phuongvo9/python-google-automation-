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
    # Length is not valid
    if len(yourpass) < 6 or len(yourpass) > 16:
        return False
    # not have any character in [a-z] - use rawstring from coursera
    elif not re.match (r"[a-zA-Z0-9$#@]", yourpass):
        return False


    # # not have any character in [A-Z]
    # elif not re.match (r"[A-Z]", yourpass):
    #     return False
    # # not have any character in [0-9]
    # elif not re.match (r"[0-9]", yourpass):
    #     return False
    
    # elif not re.match (r"[$#@]", yourpass):
    #     return False

    return True



if __name__ == '__main__':
    yourpass = input()
    if isGoodpassword(yourpass):
        print ("YES")
    else:
        print ("NO")