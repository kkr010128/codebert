# -*- coding: utf-8 -*-
while 1:
 s = raw_input()
 if s=="-": break
 n = input()
 t = 0
 for i in xrange(n): t += input()
 l = len(s)
 t %= l
 print s[t:l] + s[0:t]