# Logical error as code works but its wrong outcome
def is_even(number):
    return number % 2 == 0

print(is_even(4))

# Assertion Errors
assert 2 + 2 == 5 # Will give Error

# Syntax Error
print("Hello" # Will give a syntax error for ( <-- was never closed
      
# Exception (Runtime Errors)

# Standard Exception
## IndexError: Raised when a sequence subscript is out of range
my_list = [1, 2, 3]
print(my_list[3]) # ranges from 0-2 so out of range

## Key Error: Raised whenm a dict key is not found.
my_dict = {
    'name': 'John'
}
print(my_dict['age']) # KeyError as no age in dict

## ValueError: Raised when a function receives an argument of the correct type but inappropriate value
int("abc")

## TypeError: Raised when an operation or function receives an argument of an inappropriate type
print("Hello" + 1) or print(len(123))

# Attribute Errors: Raised when an attribute reference or assignment fails
NoneType = None
NoneType.abc

# Zero Division Error: Raised when the second operand of a division or modulo operation is zero
print(10 / 0) 

# File not found Error: Raised when trying to open a file that does not exist
open("abc.txt")
 
# OS Errors: Raised for system-related Errors, like "disk full"

# User-defined Exceptions: Define an error yourself (Users create by subclassing the built-in Exeption class)
class myCustomError(Exception):
    pass
    
raise myCustomError("Hey mate! Something went wrong!")


########
from module_1 import function_A

function_A.execute()