N = int(input())
A = list(map(int, input().split()))

L = [i+A[i] for i in range(N)]
R = [i-A[i] for i in range(N)]

p = {}
m = {}
for i in range(N):
    if L[i] not in p:
        p[L[i]] = 1
    else:
        p[L[i]] += 1
for i in range(N):
    if R[i] not in m:
        m[R[i]] = 1
    else:
        m[R[i]] += 1

lower = max(min(p), min(m))
upper = min(max(p), max(m))
ans = 0
for x in range(lower, upper + 1):
    if x in p and x in m:
        ans += p[x] * m[x]

print(ans)