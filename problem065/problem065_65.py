import sys

p = 0
s = 0
for line in sys.stdin:
    ls = line.strip('\n')
    if ls == 'END_OF_TEXT': break
    ls = ls.lower()
    if p == 0:
        w = ls
        p = 1
    else:
        for word in ls.split():
            if word == w: s += 1
print s