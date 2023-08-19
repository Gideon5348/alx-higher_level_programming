#!/usr/bin/python3

def magic_calculation(a, b):
    c = 0
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
    else:
        c = sub(a, b)
    return c
