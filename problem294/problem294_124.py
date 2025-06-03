import bisect

N = int(input())
L = list(map(int,input().split()))

ans = 0
L = sorted(L)

for i in range(N):
    for j in range(N):
        if i >= j:
            continue
        a = L[i]
        b = L[j]
        c = bisect.bisect_left(L,a+b)
        ans += c - j - 1

print(ans)