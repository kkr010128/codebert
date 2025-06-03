N = int(input())
L = list(map(int, input().split()))
L.sort(reverse=True)
ans = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        ok = i
        ng = N
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if L[mid] > L[i] - L[j]:
                ok = mid
            else:
                ng = mid
        if ok > j:
            ans += ok - j
            
print(ans)

