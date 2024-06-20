# T1W8-Thursday

# 4 Pillars of OOP (cont)
- Banking system

# __repr__ method
- Special method like __init__, which is used to define a string representation for an object.
- Particularly used for debugging and development becuase it can give detailed info about an object.

# Compostition of OOP
- Design principle where a class is composed of one or more objects from other classes.
- It's an alternative to Inheritance and is often more flexible and modular.
- Avoids inheitance's pitfall: Changes in base class can unintentially affect the derived class, which may break their functionality.
- Composition does not directly affect the composed class, as the class inherits with component classes through well-defined interfaces.

# Error Handling 
## Taxonomy of python errors
- Silent Logical Errors - Codes that run fine but logically incorrect. 
- Assertion Errors - Raised when "assert" statement fails. If condition is true nothing happens, if false raises assertion error.
- Syntax Errors - Errors in the written syntax that python interpreter cannot understand.
- Exceptions - Runtime error which occurs during program execution. Python has built in exceptions to handle common errors. 

# Stack trace Interpretation
- Text that appears when python encounters an exception, "stack trace"
- When exception occurs, the interpreter prints a stack trace that shows where the error happened and how the code rewached that point.
- Start with: Exception, then the trace.

# Try / Except / Finally
- Comprehensive way to handle exceptions.
- Ensures code always runs, regardless whether an error occurs. 
- 'try' block has code that may raise exceptions.
- 'except' block has code that handles the exception.
- 'finally' block has the code that should always be executed. 
