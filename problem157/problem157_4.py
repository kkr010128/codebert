from collections import Counter


n = int(input())
A = list(map(int, input().split()))

X = Counter([i - a for i, a in enumerate(A)])

ans = 0
for i, a in enumerate(A):
    X[i - a] -= 1
    ans += X[i + a]

print(ans)
