#!/usr/bin/python3

for c in range(122, 96, -1):
    if c % 2 == 0:
        print("{:c}".format(c - 32), end="")
    else:
        print("{:c}".format(c), end="")
