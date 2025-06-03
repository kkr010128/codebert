import math
N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
a, b = 0, 0
A, B = set(), set()
for i in range(N):
    n = N - i - 1
    m = P[i] - i - 1
    for ai in A:
        if ai < P[i]:
            m -= 1
    a += m * math.factorial(n)
    A.add(P[i])
for i in range(N):
    n = N - i - 1
    m = Q[i] - i - 1
    for bi in B:
        if bi < Q[i]:
            m -= 1
    b += m * math.factorial(n)
    B.add(Q[i])
print(abs(a - b))