iple Choice Questions

### Question 1: Which task can you accomplish by using regular expressions in log analysis?  
- [ ] Sorting log entries based on timestamps  
- [ ] Counting the total number of log entries in a file  
- [ ] Converting log data into graphical charts  
- [x] Parsing log entries to extract specific fields  


---

### Question 2: What will the following command return?  
`grep ticky syslog.log`  

- [ ] All the INFO logs in syslog  
- [ ] A duplicate file of syslog  
- [x] All the logs from ticky  
- [ ] All the ERROR logs in syslog  


---

### Question 3: Complete the sentence for the following Python regular expression: To match a string stored in a line variable, we use the `search()` method by defining a _____.  
- [ ] line  
- [ ] log  
- [x] pattern  
- [ ] span  


---

### Question 4: When sorting this dictionary:  
```python
fruit = {"oranges": 3, "apples": 5, "bananas": 4, "pears": 2}
```  
What will the following line of code return?  
```python
sorted(fruit.items(), key=operator.itemgetter(1))
```  

- [ ] [('bananas', 4), ('apples', 5), ('oranges', 3), ('pears', 2)]  
- [ ] sorted fruit = {"oranges": 3, "apples": 5, "bananas": 4, "pears": 2}  
- [ ] [('apples', 5), ('bananas', 4), ('oranges', 3), ('pears', 2)]  
- [x] [('pears', 2), ('oranges', 3), ('bananas', 4), ('apples', 5)]  

*Explanation:* The `sorted()` function sorts the dictionary items by the second value (quantity) in ascending order.

---

### Question 5: Which of the following is a potential pitfall of automation in Python?  
- [ ] It makes the system more prone to errors  
- [ ] It increases the amount of manual work required  
- [x] It limits the system's ability to adapt to changes  
- [ ] It improves the overall efficiency of the system  

**Answer:** It limits the system's ability to adapt to changes  
*Explanation:* Automation can make systems rigid and less adaptable to changes if not designed with flexibility in mind.

---

### Question 6: Which of the following is true about using regular expressions?  
- [x] They can simplify complex string processing tasks  
- [ ] They don’t allow for flexible pattern matching in strings  
- [ ] They reduce the need for error checking in code  
- [ ] They can be used only in Python  


---

### Question 7: What would you expect the command `grep "ERROR" syslog.log` to return?  
- [ ] All logs in syslog.log  
- [ ] All ERROR logs in syslog.log that have no corresponding error message  
- [x] All ERROR logs in syslog.log  
- [ ] The ERROR messages in syslog.log  


---

### Question 8: What is the Python module used to perform similar tasks to the Unix command `grep` for filtering log data?  
- [x] `re` (Regular Expression) module  
- [ ] `grep` module  
- [ ] `logfilter` module  
- [ ] `logsearch` module  

---

### Question 9: Evaluate the following problem statement: “I want to create a script to sort files.” What's missing?  
- [ ] The problem statement does not specify the programming language.  
- [ ] The problem statement does not specify what the script is supposed to do.  
- [ ] The problem statement is complete.  
- [x] The problem statement does not specify what files to sort.  

---

### Question 10: Which of the following commands would convert a CSV file named `error_message.csv` into an HTML file named `errors.html`?  
- [ ] `/html_to_csv.py error_message.csv /var/www/html/<errors>.html`  
- [ ] `/csv_to_html.py error_message.csv /var/www/html/<errors.html>.html`  
- [x] `./csv_to_html.py error_message.csv /var/www/html/<errors>.html`  
- [ ] `/csv_convert_html.py error_message.csv /var/www/html/<errors>.html`  

---