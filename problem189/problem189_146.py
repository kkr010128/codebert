from itertools import combinations

N,M = map(int,input().split())

a=["A" for i in range(0,N)]
b=["B" for i in range(0,M)]

tmp1=(len(list(combinations(a,2))))
tmp2=(len(list(combinations(b,2))))

print(tmp1+tmp2)