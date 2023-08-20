#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    max_score = -1
    best_student = None

    for student, score in a_dictionary.items():
        if score > max_score:
            max_score = score
            best_student = student

    return best_student
