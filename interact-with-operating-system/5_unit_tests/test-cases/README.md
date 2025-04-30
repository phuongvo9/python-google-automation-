# Test cases
The building blocks of unit tests within the unittest module are test cases, which enable developers to run multiple tests at once. To write test cases, developers need to write subclasses of TestCase or use FunctionTestCase. 

To perform a specific test, the TestCase subclass needs to implement a test method that starts with the name test. This identifier is what informs the test runner about which methods represent tests
```python
import unittest


class TestStringMethods(unittest.TestCase):


    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')


    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError): 
            s.split(2)


if __name__ == '__main__':
    unittest.main()
```

# Assertions
The TestCase class also employs its own assert methods that work similarly to the assert statement: if a test fails, an exception is raised with an explanatory message, and unittest identifies the test case as a failure. In the above example, there are several assertions used:

An assertEqual() to check for an expected result

An assertTrue() and an assertFalse() to verify a condition

An assertRaises() to verify that a specific exception gets raised

Each of these assert methods is used in place of the standard assert statement so the test runner can gather all the test results and generate a report


Below is a list of commonly used assert methods in the TestCase class. For more information on each method, select the embedded link in the list provided.    

The 
assertEqual(a, b)
 method checks that a == b

The 
assertNotEqual(a, b)
 method checks that a != b

The 
assertTrue(x)
 method checks that bool(x) is True

The 
assertFalse(x)
 method checks that bool(x) is False

The 
assertIs(a, b)
 method checks that a is b

The 
assertIsNot(a, b)
 method checks that a is not b

The 
assertIsNone(x)
 method checks that x is None

The 
assertIsNotNone(x)
 method checks that x is not None

The 
assertIn(a, b)
 method checks that a in b

The 
assertNotIn(a, b)
 method checks that a not in b

The 
assertIsInstance(a, b)
 method checks that isinstance(a, b)

The 
assertNotIsInstance(a, b)
 method checks that not isinstance(a,  

You can also use assert methods to generate exceptions, warnings, and log messages. For example, another important assert method in unit testing is assertRaises. It allows you to test whether exceptions are raised when they should be, ensuring that your program can handle errors. assertRaises also allows developers to check which specific exception type is raised, ensuring that the correct error handling is in place

# Commmand-line interface
Command-line interface
The command-line interface allows you to interact with an application or program through your operating system command line, terminal, or console by beginning your code with a text command. When you want to run tests in Python, you can use the unittest module from the command line to run tests from modules, classes, or even individual test methods. This also allows you to run multiple files at one time. 

To call an entire module:

python -m unittest test_module1 test_module2 

To call a test class:

python -m unittest test_module.TestClass

To call a test method:

python -m unittest test_module.TestClass.test_method

Test modules can also be called using a file path, as written below:

python -m unittest tests/test_something.py


# Unit test design patterns
One pattern that you can use for unit tests is made up of three phases: arrange, act, and assert. Arrange represents the preparation of the environment for testing; act represents the action, or the objective of the test, performed; and assert represents whether the results checked are expected or not. 

Imagine building a system for a library. The objective is to test whether a new book can be added to the library's collection and then to check if the book is in the collection. Using the above structure of arrange, act, and assert, consider the following example code:

What’s given (arrange): A library with a collection of books

When to test (act): A new book is added to the collection

Then check (assert): The new book should be present in the library's collection
```python
class Library:
	def __init__(self):
		self.collection = []

	def add_book(self, book_title):
		self.collection.append(book_title)

	def has_book(self, book_title):
		return book_title in self.collection

# Unit test for the Library system
class TestLibrary(unittest.TestCase):

	def test_adding_book_to_library(self):
    	# Arrange
		library = Library()
		new_book = "Python Design Patterns"

    	# Act
    	library.add_book(new_book)

    	# Assert
    	self.assertTrue(library.has_book(new_book))

# Running the test
library_test_output = unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestLibrary))
print(library_test_output)
```
