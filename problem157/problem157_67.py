n = int(input())
a = list(map(int,input().split()))
import collections
p = []
q = []
d = collections.defaultdict(int)
e = collections.defaultdict(int)
for i in range(n):
    p.append(a[i]+i+1)
for i in range(n):
    q.append(-a[i]+i+1)
ans = 0
for i in range(n):
    d[p[i]] += 1
    e[q[i]] += 1
for i in d.keys():
    ans += d[i]*e[i]
print(ans)