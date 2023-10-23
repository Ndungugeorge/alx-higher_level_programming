#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the division of a by b."""
    try:
        quotent = a / b
    except (TypeError, ZeroDivisionError):
        quotent = None
    finally:
        print("Inside result: {}".format(quotent))
    return (quotent)
