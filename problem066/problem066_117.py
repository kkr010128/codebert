# -*- coding: utf-8 -*-
import sys
lines = sys.stdin.readlines()
l = 0
while not ("-" in lines[l]):
 s = lines[l].replace('\n','')
 n = int(lines[l+1])
 l += 2
 t = sum(map(int, lines[l:l+n])) % len(s)
 print s[t:]+s[:t]
 l += n