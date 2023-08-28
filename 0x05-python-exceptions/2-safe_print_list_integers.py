#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed_integers = 0
    i = 0

    try:
        while i < x:
            if isinstance(my_list[i], int):
                if printed_integers > 0:
                    print(" ", end="")
                print("{:d}".format(my_list[i]), end="")
                printed_integers += 1
            i += 1
    except IndexError:
        pass

    print()
    return printed_integers
