# -*- coding: utf-8 -*-
str = raw_input()
s = ""
for c in str:
 s += (c.lower() if c.isupper() else c.upper())
print s