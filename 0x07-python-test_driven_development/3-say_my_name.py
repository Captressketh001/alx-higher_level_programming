#!/usr/bin/python3

"""A function that prints a name"""

def say_my_name(first_name, last_name=""):
    """Prints the first_name and last_name
    
    Args:
        first_name: The first parameter which must be a string
        last_name: The second parameter which must be a string too
    Raises:
        TypeError: if first_name is not string
        TypeError: if last_name is not string
    Prints:
         My name is <first_name> <last_name>
    """
    if not (isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if not (isinstance(last_name, str)):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))