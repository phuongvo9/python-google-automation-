## Reading and Writing Files
### Programming with Files
File systems are usually organized in a __tree structure__ with directories and files nested under their parents.
* A relative paths use only a portion of a path to show where the resource is located in relation to the current working directory.
* An absolute path is a full path to the resource in the file system.

### Reading Files
Read that data from files.
* **readline method** reads a single line of a file and updates the current position in the file.
* **read method** reads from the current position until the end of the file instead of just one line.

---

## Managing Files and Directories
### Working with Files
**os module** provides a layer of abstraction between Python and the operating system

Some of the functions available from the os module are: 
* remove function deletes a file
    * Trying to remove the file that doesn't exist, the function will raise an error.
* exists function checks whether a file exist
* rename function changes name of a file
    * The first parameter to rename function is the old name of the file and the second is new name.

# Useful functions
* getsize checks a file size and returns the file size in bytes.
* getmitime checks when the file was last modified and returns Unix timestamp.
* abspath function takes a filename and turns it into an absolute path.

**datetime module** provides a function to convert the Unix timestamp.

