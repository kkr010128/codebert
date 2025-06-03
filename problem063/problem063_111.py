import sys

alp = "abcdefghijklmnopqrstuvwxyz"
s = []
for line in sys.stdin:
    s += line.lower()
for i in alp:
    print(i + " : " +str(s.count(i)))