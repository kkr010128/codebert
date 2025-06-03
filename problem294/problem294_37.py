import bisect
n = int(input())
L = list(map(int, input().split()))
#%%
L.sort()

ans = 0
for i in range(n-2): # aを固定
    for j in range(i+1, n-1): # bを固定
        ab = L[i] + L[j]
        idx = bisect.bisect_left(L, ab, lo=j)
        ans += max(idx - (j+1), 0)

print(ans)
