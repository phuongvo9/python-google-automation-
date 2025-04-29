# Compare `unittest` and `pytest`


| Feature                     | `unittest`                                                                 | `pytest`                                                                 |
|-----------------------------|---------------------------------------------------------------------------|-------------------------------------------------------------------------|
| **Built-in or External**    | Built into Python                                                         | Requires external installation (`pip install pytest`)                  |
| **Test Discovery**          | Must be called from the command line to detect test cases automatically   | Automatically detects tests with the `test_` prefix                    |
| **Programming Approach**    | Object-oriented approach                                                  | Functional approach                                                    |
| **Assertions**              | Uses special methods like `assertEqual()` and `assertTrue()`              | Uses Python's built-in `assert` statements                             |
| **Readability**             | Slightly more verbose due to special assertion methods                   | Easier to read and write due to simpler assertion syntax               |
| **Backward Compatibility**  | Built into Python, ensuring compatibility                                 | Compatible with `unittest`, allowing gradual adoption                  |

