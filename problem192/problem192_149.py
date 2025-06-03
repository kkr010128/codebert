import sys
import collections
ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
a = rl()
c = collections.Counter(a)
t = 0
for v in c.values():
    t += v*(v-1)//2

for i in a:
    print(t-c[i]+1)
