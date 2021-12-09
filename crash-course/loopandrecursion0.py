


# Back to basics first!

# x = 0
# while x < 5:
#     print ("Not there yet, x=" + str(x))
#     x = x + 1

# print ("x= " + str(x))

def attempts (n):
    x = 1
    while x <=n:
        print ("Attempt " +str(x))
        x += 1
    print ("Done")

#attempts(9)


# ------- Initializing variables matters !! ---

def count_down(start_number):
    current = start_number
    while (current > 0):
        print (str(current))
        current = current - 1
    
    print ("Zero!")

#count_down (1)


"""
Find smallest prime factor that is a divisor of x
"""

def smallest_prime_factor(x):
    """ Return smallest prime number that is a divisor of x"""
    # start checking with 2, then move up one by one
    n = 2
    while n <=  x:
        if x % n == 0:
            return n
        n += 1

print(smallest_prime_factor(5)) # should be 5
print(smallest_prime_factor(15)) # should be 3
print(smallest_prime_factor(19)) # should be 19
print(smallest_prime_factor(12)) # should be 2

"""
In math, the factorial of a number is defined as the product of an integer and all the integers below it. For example, the factorial of four (4!) is equal to 1*2*3*4=24.
Let's make the factorial function return the right number.
"""
def factorial(n):
    result = 1
    for i in range (1,n+1):
        result = result * i
    return result
