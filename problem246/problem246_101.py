from itertools import permutations
n = int(input())
p = tuple(map(int,input().split()))
q = tuple(map(int,input().split()))

per = [0] + list(permutations(list(range(1,n+1))))
pnum = per.index(p)
qnum = per.index(q)
ans = abs(pnum-qnum)

print(ans)