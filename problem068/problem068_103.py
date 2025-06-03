# -*- coding: utf-8 -*-
str = raw_input()
for _ in xrange(input()):
 ops = raw_input().split()
 na = int(ops[1])
 nb = int(ops[2]) + 1
 op = ops[0]
 if op[0]=="p": print str[na:nb]
 elif op[2]=="v":
  t = str[na:nb]
  str = str[:na] + t[::-1] + str[nb:]
 else: str = str[:na] + ops[3] + str[nb:]