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