# -*- coding: utf-8 -*-
'import sys'
input()
a=[int(i) for i in input().split()]
a.reverse()
f=0
for i in range(len(a)):
    if f: print(" ",end="")
    print("{}".format(a[i]),end="")
    f=1
print("")