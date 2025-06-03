import itertools
N=int(input())
L=list(map(int,input().split()))
c=0
if len(L) >=3:
    for v in itertools.combinations(L, 3):
        if (v[0] != v[1] and v[1] != v[2]) and v[0] != v[2]:
            if sorted(v)[-2]+min(v) > max(v):
                c=c+1
            else:
                c=c
        else:
            c=c
else:
    c=0
print(c)