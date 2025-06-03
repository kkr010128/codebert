def solve(A, i, m, n):
    """Return if it is possible to make value m with some elements in A.

    n is length of A.
    i is index.
    R is the record of answer i, m.
    Using Divide-and-Conquer method.
    """

    if R[i][m] != None:
        return R[i][m]
    if m == 0:
        R[i][m] = True
        return True
    elif i >= n:
        R[i][m] = False
        return False
    else:
        ans = solve(A, i + 1, m, n) or solve(A, i + 1, m - A[i], n)
        R[i][m] = ans
        return ans


import sys

n = int(sys.stdin.readline())
A = tuple(map(int, sys.stdin.readline().split()))
q = int(sys.stdin.readline())
M = tuple(map(int, sys.stdin.readline().split()))

s_A = sum(A)
R = [[None] * 2000 for i in range(n + 1)]

ans = ''

for m in M:
    if s_A < m:
        ans += 'no\n'
    elif solve(A, 0, m, n):
        ans += 'yes\n'
    else:
        ans += 'no\n'

print(ans, end = '')