import copy
from collections import deque
n, m, q = list(map(int, input().split()))

abcd = []
for _ in range(q):
    abcd.append(list(map(int, input().split())))

ans = 0
def dfs(A, low, high, n):
    global ans
    if len(A) >= n:
        result = 0
        for a,b,c,d in abcd:

            if A[b-1]-A[a-1] == c:
                result += d
        ans = max(ans, result)
        return

    for i in range(low, high+1):
        A.append(i)
        dfs(A, i, high, n)
        A.pop()

dfs([], 1, m, n)
print(ans)
