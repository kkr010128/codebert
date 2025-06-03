from sys import stdin
import math
inp = lambda : stdin.readline().strip()

s = inp()
if s[2] == s[3] and s[4] == s[5]:
    print("Yes")
else:
    print("No")