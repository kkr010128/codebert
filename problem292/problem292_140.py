n=int(input())
d = list(map(int,input().split()))
import itertools
p = itertools.combinations(d, 2)
s=0
for v in p:
    s+=v[0]*v[1]
print(s)