import sys

cnt = {}

for line in sys.stdin:
    for c in line:
        if c.isalpha():
            cl = c.lower()
            cnt[cl] = cnt.get(cl, 0) + 1

for i in range(97, 97 + 26):
    c = chr(i)
    print("{0} : {1}".format(c, cnt.get(c, 0)))
