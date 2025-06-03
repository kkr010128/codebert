n = int(input())
A = list(map(int, input().split()))

from collections import Counter
C = Counter(A)

X = [0]*(10**6+1)
A = list(set(A))
A.sort()
ans = 0
for a in A:
    if X[a] == 0 and C[a] == 1:
        ans += 1
    X[a] += 1
    j = 2*a
    while j <= 10**6:
        X[j] += 1
        j += a
print(ans)
