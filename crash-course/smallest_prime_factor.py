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