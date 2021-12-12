#!/usr/bin/env python3

def format_address (address_string):
    house_number = ""
    street_name = ""
    
    my_address = address_string.split()
    for i in my_address:
        if i.isdigit():
            house_number = i
        else:
            street_name = i
    return "house number {} on stree named {}".format(house_number,street_name)


print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"