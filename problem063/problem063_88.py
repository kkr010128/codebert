import sys
s = sys.stdin.read()
for c in [chr(i) for i in range(97,97+26)]:
    print(c, ":", s.lower().count(c))