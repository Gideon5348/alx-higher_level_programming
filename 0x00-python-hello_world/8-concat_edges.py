#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[str.index("object"):str.index("object") + 27] + str[str.index("Python"):str.index("Python") + 6]
print(str)
