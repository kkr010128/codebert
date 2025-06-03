# coding: utf-8

string = raw_input()
new_string = ""
for s in string:
    if s.islower():
        new_string += s.upper()
    elif s.isupper():
        new_string += s.lower()
    else:
        new_string += s
print new_string