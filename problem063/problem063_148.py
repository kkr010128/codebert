import sys
d=[0 for i in range(26)]
for line in sys.stdin:
    for c in line:
        x = ord(c)
        if ord('A')<=x and x<=ord('Z'):
            x -= (ord('A')-ord('a'))
        if ord('a')<=x and x<=ord('z'):
            d[x-ord('a')] += 1   

for i in range(26):
    print("%s : %d" % (chr(ord('a')+i),d[i]))