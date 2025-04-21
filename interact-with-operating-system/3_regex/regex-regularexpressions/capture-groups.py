#!/usr/bin/env python3

# Capture groups in regex
import re
result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)
print(result.groups())
print(result[0])
print(result[1])
print(result[2])
"{} {}".format(result[2], result[1])


def rearrange_name(name):
    """
    Rearranges a name from "Last, First" to "First Last"
    Explains the use of capture groups in regex
    :param name: str, name in the format "Last, First"
    :return: str, name in the format "First Last"
    :example: rearrange_name("Lovelace, Ada") -> "Ada Lovelace"
    """
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])
rearrange_name("Lovelace, Ada")

def rearrange_name_two(name):
    """
    Rearranges a name from "Last, First" to "First Last"
    Explains the use of capture groups in regex
    :param name: str, name in the format "Last, First"
    :return: str, name in the format "First Last"
    :example: rearrange_name_two("Ritchie, Dennis") -> "Dennis Ritchie"
    """
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])
rearrange_name_two("Ritchie, Dennis")

def rearrange_name_three(name):
    """
    Rearranges a name from "Last, First" to "First Last"
    Explains the use of capture groups in regex
    :param name: str, name in the format "Last, First"
    :return: str, name in the format "First Last"
    :example: rearrange_name_three("Hopper, Grace M.") -> "Grace M. Hopper"
    """
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])
rearrange_name_three("Hopper, Grace M.")