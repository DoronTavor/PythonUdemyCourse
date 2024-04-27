#
# 1. LINTING
# num +4 - The pycharm lints our code
#
# 2. USE IDE/ editor-Recommend IDE for python
#
# 3. READ ERRORS
# 5555+ 'gdfgfsdgf' will give the error- Traceback (most recent call last):
#   File "C:\Users\tavor\PycharmProjects\PythonUdemyCourse\DEBUGING_LEARNING.py", line 8, in <module>
#     4+ 'gdfgfsdgf'
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
#     We should understand the errors and their types, and from that we need to try to fix out problem.
#
# 4. PDB- built in python module for debugging
import pdb
def add(num1,num2):
    pdb.set_trace()
    return num1+num2
add(4,"5")