# -*- coding: utf-8 -*-

n = int(raw_input())
dic = set()
for i in range(n):
    com, s = map(str, raw_input().split())
    if com == "insert":
        dic.add(s)
    elif com == "find":
        if s in dic:
            print "yes"
        else:
            print "no"