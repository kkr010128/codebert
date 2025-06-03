from itertools import combinations_with_replacement
n,m,q = map(int,input().split())
ans = -1
li = [tuple(map(int,input().split())) for i in range(q)]
for K in combinations_with_replacement(range(1,m+1),n):
    s = 0
    for a,b,c,d in li:
        a -= 1
        b -= 1
        if K[b]-K[a] == c:
            s += d
    ans = max(ans,s)
print(ans)