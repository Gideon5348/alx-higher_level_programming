#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
import json
from json import dump, load


def load_from_json_file(filename):
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            data = load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    return data


# Function to save data to a JSON file
def save_to_json_file(data, filename):
    with open(filename, mode="w", encoding="utf-8") as file:
        dump(data, file)


# Check if the file add_item.json exists and load its contents
filename = "add_item.json"
my_list = load_from_json_file(filename)

# Append command line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list back to add_item.json
save_to_json_file(my_list, filename)
