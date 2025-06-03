import sys
s = sys.stdin.read().lower()
for i in range(ord("a"), ord("z")+1):
    print(chr(i), ":", s.count(chr(i)))
