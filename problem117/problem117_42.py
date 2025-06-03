import bisect
N, M, K = map(int, input().split())
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))

Asums = [0] * (N + 1)
for i, a in enumerate(A):
    Asums[i+1] = Asums[i] + a

Bsums = [0] * (M + 1)
for i, b in enumerate(B):
    Bsums[i+1] = Bsums[i] + b

ans = 0
for anum in range(N + 1):
    t = Asums[anum]
    if K < t:
        break
    bnum = bisect.bisect_right(Bsums, K - t) - 1
    ans = max(ans, anum + bnum)
print(ans)