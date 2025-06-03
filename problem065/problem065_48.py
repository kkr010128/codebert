# -*- coding: utf-8 -*-
w = raw_input().upper()
c = 0
while 1:
 t = raw_input()
 if t=="END_OF_TEXT": break
 c += t.upper().split().count(w)
print c