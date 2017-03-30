# Test-Python

### How to Use?
Test-Python uses **tp-config.json** file to read test cases from there is a demo *tp-config.json* to to learn the structure from.
Now the test.py script tests the testcode.py against the testcases present in tp-config.json.

### Usage
* Testing Whole project
``` 
python3 test.py 
```
* Testing a specific module in a function
``` 
python3 test.py -m module-name 
```
* Testing a specific function in a specific module
``` 
python3 test.py -m module-name  -f function-name 
```
