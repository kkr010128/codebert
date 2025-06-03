N, M, K = map(int, input().split())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

total = 0
Asum = sum(A)
nA = len(A)
Bsum = 0
ans = 0
for nB in range(len(B) + 1):
    if nB != 0:
        Bsum += B[nB-1]
    if Bsum > K:
        break
    while Asum + Bsum > K:
        nA -= 1
        Asum -= A[nA]
    ans = max(nA + nB, ans)

print(ans)
