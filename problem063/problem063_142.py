# coding:utf-8
import sys
a = []
for line in sys.stdin:
    a.append(list(line.strip().replace(" ","").lower()))
a = reduce(lambda x,y: x+y,a)
dict = {}
for i in range(26):
    dict[chr(ord('a')+i)] = 0
for i in a:
    for key,value in dict.items():
        if key == i:
            dict[key] += 1
for key,value in sorted(dict.items()):
    print "%s : %d" % (key,value)

