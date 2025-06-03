N = int(input())
slist = []
tlist = []
from itertools import accumulate
for _ in range(N):
    s, t = input().split()
    slist.append(s)
    tlist.append(int(t))
cum = list(accumulate(tlist))
print(cum[-1]-cum[slist.index(input())])
