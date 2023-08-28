#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
  i = 0
  nb_print = 0
  try:
    while i < x:
      if isinstance(my_list[i], int):
        print("{:d}".format(my_list[i]), end="")
        nb_print += 1
      i += 1
  except IndexError:
    pass
  print()
  return nb_print
