#Quiz

def format_name (first_name,last_name):
    # code goes here
    string = 'Name:' + ', ' .join([name for name in [last_name, first_name] if name]) if any([last_name, first_nam]) else ''
    return string

print (format_name ("Ernest","Hemingway"))
# Should return "Name: Hemingway, Ernest"

print (format_name("","Madona"))
# Should return "Name: Madona"

print(format_name("Voltair",""))
# Should return "Name: Voltaire"

print(format_name("",""))
#Should return an empty string

