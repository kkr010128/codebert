from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))

dd = defaultdict(int)

ans = 0
for i in range(n):
    diff = i - A[i]
    ans += dd[diff]
    summ = A[i] + i
    dd[summ] += 1

print(ans)
