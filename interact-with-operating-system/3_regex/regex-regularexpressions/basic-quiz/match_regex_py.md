Which of the following functions are used to match a regular expression pattern in Python? Select all correct answers. 


re.findall()  
re.match()
re.find()  
re.search()
The correct answers are:
- re.findall()
- re.match()
- re.search()

---

Question 2
Which method from the csv module is used to write rows of data into a CSV file? 


csv.writerows()
csv.add_rows()
csv.write_rows()
csv.write()

The correct answer is: 
- csv.writerows()

----

Question 3
You are reading an article that contains website urls in the format: 

https://www.website-domain.com

You’d like to extract the complete urls from the text automatically, instead of copying and pasting them by hand. Complete the function find_url() to extract all encrypted websites that begin with https:// and end with any top level domain, such as .org, .com, or .co from the text.

```python
def find_url(website):
 pattern = _____#enter the regex pattern here
 result = re._____(pattern, website) #enter the re method here
 return result


print(find_url("Go to the website https://www.coursera.com find more information about Google Certificate Programs. Then, visit https://www.python.org/ to learn more about Python. ")) # Should return ['https://www.coursera.com', 'https://www.python.org']
print(find_url("You can find anything on https://www.google.com!")) # Should return ['https://www.google.com']
print(find_url("You can find anything on http://www.google.com!")) # Should return []
print(find_url("Check out python.org!")) # Should return []
```

The correct answer is:
```python
def find_url(website):
 pattern = r'https://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
 result = re.findall(pattern, website)
 return result
```

Explaination:
- The regex pattern `r'https://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'` matches any string that starts with `https://`, followed by any combination of alphanumeric characters, dots, or hyphens, and ends with a dot followed by at least two alphabetic characters (representing the top-level domain).
    - + means one or more characters
    - [a-zA-Z0-9.-] matches any alphanumeric character, dot, or hyphen
    - \. is used to escape the dot, as it has a special meaning in regex
    - [a-zA-Z]{2,} matches any alphabetic character (upper or lower case) and the {2,} quantifier specifies that there must be at least 2 characters
- The `re.findall()` method is used to find all occurrences of the pattern in the input string


---

You are exploring the punctuation at the end of sentences and want to split sentences so that each word is separate and any punctuation is included in the word next to it. Complete the parse_sentences() function to accomplish this task. 
```python
def parse_sentences(sentence):
 pattern =_______ #enter the regex pattern here
 result = re._____(pattern, sentence) #enter the re method  here
 return result

print(parse_sentences("Hello! How are you doing?")) # should return ['Hello!', 'How', 'are', 'you', 'doing?']
print(parse_sentences("what a beautiful day it is")) # should return ['what', 'a', 'beautiful', 'day', 'it', 'is']
print(parse_sentences("2 + 2 is definitely 4!")) # should return ['2', '+', '2', 'is', 'definitely', '4!']
```

The correct answer is:
```python
def parse_sentences(sentence):
 pattern = r'\w+|[^\w\s]'
 result = re.findall(pattern, sentence)
 return result
```
Explaination:
- The regex pattern `r'\w+|[^\w\s]'` matches any word character (alphanumeric or underscore) one or more times, or any character that is not a word character or whitespace.
    - \w+ matches one or more word characters
    - | is the OR operator
    - [^\w\s] matches any character that is not a word character or whitespace

---

Question 5
A company uses Product ID numbers to identify each product line it makes. Each product ID starts with 4 digits, followed by a hyphen (-), followed by two capital letters, followed by a hyphen (-), followed by two more digits, in the format: 

1234-AB-12 

The manufacturing team records information about the production of each product line daily. You want to extract the product ID numbers of one of these product lines, which begins with a 1. The other characters in the product ID can be any digit or variable, as long as they follow the product ID format described above. Complete the following code so the find_productID() function returns all product ID numbers that match the product of interest. 

```python
def find_productID(report):
  pattern = r'1\d{3}-[A-Z]{2}-\d{2}' #enter the regex pattern here
  result = re.findall(pattern, report) #enter the re method  here
  return result
  
print(find_productID("Products 1234-AB-30 and 2234-AB-30, not items 12-AB-30 or 12345-AB-30")) # Should return ['1234-AB-30']
print(find_productID("Products of interest are 1234-AB-30, 1678-XZ-11, and 1561-CD-57. We're not interested in other products like 2345-AB-29.")) # Should return ['1234-AB-30', '1678-XZ-11', '1561-CD-57']
```
Explaination:
- The regex pattern `r'1\d{3}-[A-Z]{2}-\d{2}'` matches any string that starts with a 1, followed by three digits, a hyphen, two uppercase letters, another hyphen, and two digits.
    - \d{3} matches exactly three digits
    - [A-Z]{2} matches exactly two uppercase letters
    - \d{2} matches exactly two digits

---

```python
def replace_domain(address, old_domain, new_domain):
  old_domain_pattern = r'' + old_domain + '$'
  address = re.sub(old_domain_pattern, new_domain, address)
  return address
```
What is the purpose of the replace_domain() function?
- To create new email address from the old domain in a given address with a new domain