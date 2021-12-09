


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


