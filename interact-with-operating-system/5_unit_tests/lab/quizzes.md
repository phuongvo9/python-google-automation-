### Question 1: What is the cause of an IndexError?
- [ ] Not specifying classes.
- [ ] Attempting to index a list with invalid parameters.
- [ ] Searching a list that contains errors.
- [x] Attempting to access an index that's outside the bounds of a list.
---


### Question 3: From a developer’s perspective, what is a good reason to write test cases for your scripts? 
- [ ] Writing a test ensures a developer’s code will be bug-free.
- [ ] Scripts will work on updated platforms as long as tests are used.
- [ ] Writing a test enables developers to write longer code.
- [x] Writing a test makes developers examine the script’s design, leading you to create better scripts in the future.

---

### Question 4: Which of the following statements accurately describe how `try/except` blocks work? (Select all that apply)
- [ ] If no exceptions occur, the `try` clause is ignored.
- [ ] If an exception occurs during the execution of the `try` clause, the `try` clause is executed and ignored.
- [x] If an exception occurs during the execution of the `try` clause, the rest of the `try` clause is then skipped.
- [x] The `try` clause is executed.


---

### Question 5: What is the purpose of software testing? 
- [ ] To prove that the software works correctly.
- [ ] To find all bugs in the software so they can be repaired.
- [x] To determine whether the software meets the specified requirements.
- [ ] To identify the features that are not needed.

---

### Question 6: When referring to unit testing, what is a “test runner”?
- [ ] A test runner automatically determines the type of clause you will need to solve an issue.
- [ ] A test runner allows a Python file to access scripts from another Python file.
- [ ] A test runner automatically determines the type of loop you will need to solve an issue.
- [x] A test runner is a component that orchestrates the execution of tests and provides an outcome.


---

### Question 7: The following code will either return an email address for an employee or an error message if there is no employee matching the name entered. What would the error message be?

```python
if email_dict.get(fullname.lower()):
    return email_dict.get(fullname.lower())
else:
    return "No email"
```

- [ ] “No employee found”
- [ ] “Missing parameters”
- [x] “No email”
- [ ] “No email address found”

---

### Question 8: Which of the following commands represent the correct sequence for catching an exception for a division by zero error in Python? 
- [ ] `try: a/b except: pass`
- [x] `try: a/b except ZeroDivisionError: pass`
- [ ] `try: a/b except: ZeroDivisionError`
- [ ] `try: a/b except ZeroDivisionError:`


---

### Question 9: The following portion of code will return an error message if a user fails to enter the full name of the employee for a search. What will the error message be?

```python
def find_email(argv):
    """ Return an email address based on the username given."""
    # Create the username based on the command line input.
    try:
        fullname = str(argv[1] + " " + argv[2])
        # Preprocess the data
        email_dict = populate_dictionary('/home/<username>/data/user_emails.csv')
        # Find and print the email
        return email_dict.get(fullname.lower())
    except IndexError:
```

- [ ] “IndexError”
- [ ] “Missing username”
- [x] “Missing name”
- [ ] “No email address found”


---

### Question 10: When writing a `try/except` clause, how many `except` clauses can be included? 
- [ ] One more `except` clause than there are specific handlers for different exceptions.
- [ ] Only one.
- [ ] As many as needed as long as there is one `try` clause per `except` clause.
- [x] As many `except` clauses are needed to specify handlers for different exceptions.

---