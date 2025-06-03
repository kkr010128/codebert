# -*- coding: utf-8 -*-

buf = str(raw_input())
char_list = list(buf)
res = ""

for i in char_list:
    if i.isupper():
        res += i.lower()
    elif i.islower():
        res += i.upper()
    else:
        res += i

print res