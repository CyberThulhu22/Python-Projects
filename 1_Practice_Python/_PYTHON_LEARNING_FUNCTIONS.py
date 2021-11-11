#!/usr/bin/env python3
#-*- Coding: utf-8 -*-

"""
NAME: Functions_Learning
VERSION: None
AUTHOR: Jesse Leverett (CyberThulhu)
STATUS: Building Initial code framework
DESCRIPTION: Collection Learning Function Building
TO-DO: None
COPYRIGHT © 2021 Jesse Leverett
"""


# Leaning Functions - Basic Function
first_arg = "This is a variable"        # This is a declared variable. This can be fed into a function. This one is a 'string'.
second_arg = True                       # This is another variable. This one will be fed into the same function. This one is a 'boolean'

# This is the start of a Function. You define a function by starting with 'def' followed by the name of the function.
# After the name of the function, you will provide an '()', this can also be where you specify any required arguments for the function
# Specifying variables would look like '(variable_one, variable_two, variable_three, and_so_on)'
# To close the defining of the function you put a ':'. Then you will go to the next line and write out what the function will do when called.
def normal_function(first_argument:str=first_arg, second_argument:bool=second_arg) -> None:
    """
    This is a Function Docstring. This is optionally used to describe the Function's purpose
    
    This function requires two arguments: first_argument and second_argument
    
    The text following the ':' after the argument is an 'annotation'.
    An annotation is optional, and is meant to serve as a easy way to ID what the expected argument type/outcome is.

    After declaring the annotation, you can also set a default for the argument by providing an '=' then what the default will be.
    You can assign a default variable if it's declared or directly. 
    For example: 
    argument=declared_variable
    argument='Hello World'

    The last part following the '->' is the functions 'annotation'.
    This helps someone reading the code to identify what to expect the function to return
    """
    try:                                # This is a try statement. It will try to complete the task, but if it fails. You can catch the 'exception'
        if second_argument:
            return first_argument
        else:
            return "The provided second argument was 'False'"
    except:                             # This is an exeption! Somehow your code failed, but this allows the code to fail gracefully instead.
            print("If your code fails") # You can specify what the code will do in the event that something catastrophically fails!
# Without the Try/Except, You're code can catastrophically fail, and this can cause a number of problems. 
# Typcially the code will abruptly stop, and close the program.

# Now that your function has been written. You have to call it to use it! Here's how:
normal_function()                       # Expected Result should be...BLANK! Why!? 
                                        # Because we only returned a value. We did nothing with that value. So Lets fix this.

print(normal_function())                # Expected Result is now 'This is a variable'. 
                                        # Because we didn't provide arguments the function used defualt functions

print(normal_function("Hello World"))   # Expected Result here is 'Hello World'!
                                        # This is because we supplied the first argument
                                        # It is important to note that the function will assign the variables in the order that you declared the arguments
