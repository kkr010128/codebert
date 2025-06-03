import math
import sys

s = list(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())

if len(set(s)) == 1:
    print(len(s) * k // 2)
    sys.exit()
ss = s * 2
tmp, tmp2 = 0, 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        tmp += 1
        s[i + 1] = '-1'
for i in range(len(s) * 2 - 1):
    if ss[i] == ss[i + 1]:
        tmp2 += 1
        ss[i + 1] = '-1'
print(tmp + (tmp2 - tmp) * (k - 1))