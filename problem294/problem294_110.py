import bisect

N = int(input())
L = [int(n) for n in input().split()]
L = sorted(L)

total = 0

for i in range(N - 2):
    a = L[i]
    for j in range(i + 1, N - 1):
        b = L[j]
        right_endpoint = bisect.bisect_left(L, a+b, j)
        total += right_endpoint - j - 1

print(total)