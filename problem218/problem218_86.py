import collections

N=int(input())
S=sorted([input() for _ in range(N)])
s=sorted(list(set(S)))
l=len(s)
c=collections.Counter(S)
max_v = max(c.values())
for i in range(l):
    if max_v==c[s[i]]:
        print(s[i])