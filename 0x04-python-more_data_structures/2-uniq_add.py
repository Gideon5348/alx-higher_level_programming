#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_numbers = set()
    total_sum = 0

    for number in my_list:
        if number not in unique_numbers:
            unique_numbers.add(number)
            total_sum += number

    return total_sum
