n, m, q = map(int, input().split())
abcd = []
for _ in range(q):
    abcd.append(tuple(map(int, input().split())))
ans = 0
from itertools import combinations_with_replacement
for A in combinations_with_replacement(list(range(1, m+1)), n):
    suma = 0
    for a,b,c,d in abcd:
        if A[b-1] - A[a-1] == c:
            suma += d
    ans = max(ans, suma)
print(ans)
