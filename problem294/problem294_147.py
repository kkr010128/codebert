n = int(input())
L = list(map(int,input().split()))
L = sorted(L)
import bisect
ans = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        a = bisect.bisect_left(L,L[i]+L[j])
        ans += a-j-1
print(ans)