from collections import defaultdict

N, K = map(int, input().split())

d = defaultdict(int)

for i in range(K):
    _ = int(input())
    A = [int(x) - 1 for x in input().split()]
    for j in range(len(A)):
        d[A[j]] += 1

ans = 0
for i in range(N):
    if d[i] == 0:
        ans += 1
print(ans)
