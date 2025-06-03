import sys
input = lambda: sys.stdin.readline().rstrip()

s = input()
n = len(s)
if n == s.count("hi")*2:
    print("Yes")
else:
    print("No")