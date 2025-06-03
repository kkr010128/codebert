# -*- coding: utf-8 -*-
str = raw_input()
for _ in xrange(input()):
 ops = raw_input().split()
 a = int(ops[1])
 b = int(ops[2]) + 1
 op = ops[0]
 if op[0]=="p": print str[a:b]
 elif op[2]=="v": str = str[:a] + str[a:b][::-1] + str[b:]
 else: str = str[:a] + ops[3] + str[b:]