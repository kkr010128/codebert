from copy import deepcopy
n, m, q = map(int, input().split())
tuples = [tuple(map(int, input().split())) for i in range(q)]
As = [[1]*n]
def next(A, i):
    if i == 0 and A[i] == m:
        return
    if A[i] == m:
        next(A, i-1)
    elif A[i] < m:
        if (i < n - 1 and A[i] < A[i+1]) or (i == n-1):
            A1 = deepcopy(A)
            A1[i] += 1
            As.append(A1)
            next(A1, i)
        if i > 0 and A[i] > A[i-1]:
            A2 = deepcopy(A)
            next(A2, i-1)
    elif i == 0:
        A1 = deepcopy(A)
        next(A1, n-1)
next([1]*(n), n-1)
def check(A):
    score = 0
    for a, b, c, d in tuples:
        if A[b-1] - A[a-1] == c:
            score += d
    return score
ans = 0
for A in As:
    score = check(A)
    ans = max(ans, score)
print (ans)