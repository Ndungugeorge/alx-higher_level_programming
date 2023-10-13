#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return
    for o in sorted(a_dictionary.keys()):
        print("{}: {}".format(o, a_dictionary.get(o)))
