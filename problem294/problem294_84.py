n = int(input())
L = list(map(int, input().split()))
L.sort()
#print(L)
import bisect
ans = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        k = bisect.bisect_left(L, L[i]+L[j])
        #print(i, j, k)
        ans += max(0, k-j-1)
print(ans)
