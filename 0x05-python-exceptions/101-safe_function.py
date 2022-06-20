#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    """
    Args:
        fct:
        args:

    Returns:
        
    """
    try:
        return fct(*args)
    except ZeroDivisionError:
        print("Exception: division by zero", file=sys.stderr)
    except IndexError:
        print("Exception: list index out of range", file=sys.stderr)
    return None
