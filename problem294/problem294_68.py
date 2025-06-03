import bisect

n = int(input())
L = list(map(int,input().split()))
L.sort()

ans = 0
for a in range(0,n):
    for b in range(a+1,n):
        p = bisect.bisect_left(L, L[a]+L[b])
        ans += max(p-(b+1),0)
        
print(ans)