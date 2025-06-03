import sys
import math

n = input()

s = [set(), set(), set(), set()]
ch = {0:"S", 1:"H", 2:"C", 3:"D"}

for i in xrange(n) :
    kind, num = raw_input().split()
    num = int(num)

    for j in xrange(4) :
        if (kind == ch[j]) :
            s[j].add(num)
            break

for i in xrange(4) :
    for j in xrange(1, 14) :
        if not(j in s[i]) :
            print ch[i], j