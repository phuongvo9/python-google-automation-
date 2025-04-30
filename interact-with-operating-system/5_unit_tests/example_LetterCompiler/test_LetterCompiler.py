import unittest

class TestCompiler(unittest.TestCase):

    def test_basic(self):
        testcase = "The best preparation for tomorrow is doing your best today."
        expected = ['b', 'a', 'a', 'b', 'a']
        self.assertEqual(LetterCompiler(testcase), expected)

# unittest.main()

unittest.main(argv = ['first-arg-is-ignored'], exit = False)

class TestCompiler2(unittest.TestCase):
    
    def test_two(self):
        testcase = "A b c d e f g h i j k l m n o q r s t u v w x y z"
        expected = ['b', 'c']
        self.assertEqual(LetterCompiler(testcase), expected)

# EDGE CASES HERE
class TestCompiler3(unittest.TestCase):
    
    def test_empty_string(self):
        testcase = ""
        expected = []
        self.assertEqual(LetterCompiler(testcase), expected)

    def test_no_matching_characters(self):
        testcase = "xyz"
        expected = []
        self.assertEqual(LetterCompiler(testcase), expected)

unittest.main(argv = ['first-arg-is-ignored'], exit = False)