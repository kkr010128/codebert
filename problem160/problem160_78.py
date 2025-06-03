import sys,itertools
input = sys.stdin.readline

N,M,Q = list(map(int,input().split()))
abcd = [ list(map(int,input().split())) for _ in range(Q)]
ans = 0

A = itertools.combinations_with_replacement(range(1,M+1),N)

for Ai in A:
    point = 0
    for a,b,c,d in abcd:
        if Ai[b-1] - Ai[a-1] == c:
            point += d
    ans= max(ans,point)
print(ans)
