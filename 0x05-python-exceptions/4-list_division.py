#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            division_result = 0
            if type(my_list_1[i]) not in (int, float) or \
               type(my_list_2[i]) not in (int, float):
                print("wrong type")
            else:
                division_result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            result.append(division_result)

    return result
