import math


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


N, M = map(int, input().split())
ans = 0
if N >= 2:
    ans += combinations_count(N, 2)
if M >= 2:
    ans += combinations_count(M, 2)
print(ans)
