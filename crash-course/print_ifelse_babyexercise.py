# Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
if __name__ == "__main__":
    n = int(input().strip())

def is_weird_n (number):
    """Return True if n is weird"""
    if not number % 2 == 0:
        return True
    elif n >=2 and n <=5:
        return False
    elif n >= 6 and n <= 20:
        return True
    else:
        return False
    
if is_weird_n(n):
    print ("Weird")
else:
    print ("Not Weird")


