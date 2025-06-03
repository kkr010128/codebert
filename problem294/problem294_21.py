import bisect

N = int(input())
L = sorted(map(int, input().split(' ')))

ans = 0
for i in range(len(L)):
    for j in range(i + 1, len(L)):
        a = L[i]
        b = L[j]
        ans += max(0, bisect.bisect_right(L, a + b - 1) - (j + 1))

print(ans)
