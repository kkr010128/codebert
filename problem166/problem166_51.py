import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


s = input()
n = len(s)
a = [None]*n
c = 0
v = 1
for i in range(n-1, -1, -1):
    c = (c + v*int(s[i])) % 2019
    a[i] = c
    v *= 10
    v %= 2019
from collections import Counter
cc = Counter(a)
ans = 0
for k,v in cc.items():
    ans += v*(v-1)//2
ans += cc[0]
print(ans)