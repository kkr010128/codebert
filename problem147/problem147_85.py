import sys
s, t = [line.rstrip("\n") for line in sys.stdin.readlines()]
if s == t[:-1]:
    print("Yes")
else:
    print("No")
