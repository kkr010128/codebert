import sys

alist = list('abcdefghijklmnopqrstuvwxyz')
r = {}
for al in alist:
    r[al] = 0

line = sys.stdin.read().lower()

for i in range(len(line)):
    if line[i] in r.keys():
        r[line[i]] += 1

for k,v in r.items():
    print("{} : {}".format(k, v))

