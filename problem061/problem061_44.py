# -*- coding: utf-8 -*-
str = raw_input()
s = []
for c in str:
 s.append(c.lower() if c.isupper() else c.upper())
print ''.join(s)