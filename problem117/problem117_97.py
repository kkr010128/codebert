N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

totalA = sum(A)
while totalA > K:
    totalA -= A.pop()
ans = len(A)

totalB = 0
for i in range(M):
    totalB += B[i]
    while totalA + totalB > K:
        if not A:
            break
        totalA -= A.pop()
    if totalA + totalB <= K:
        ans = max(ans, len(A) + i + 1)

print(ans)
