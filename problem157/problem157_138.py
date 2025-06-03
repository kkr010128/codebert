N = int(input())
A = [int(x) for x in input().split()]

L = dict(); R = dict()
for i in range(N):
    l = i + A[i]
    if l in L:
        L[l] += 1
    else:
        L[l] = 1
    r = i - A[i]
    if r in R:
        R[r] += 1
    else:
        R[r] = 1

ans = 0
for x in R:
    if x in L:
        ans += L[x] * R[x]

print(ans)