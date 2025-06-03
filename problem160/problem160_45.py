N, M, Q = map(int, input().split())
L = list(tuple(map(int, input().split())) for _ in range(Q))

ans = 0
A = []


def dfs():
    global A, ans
    if len(A) == N:
        res = sum(t[3] for t in L if A[t[1]-1] - A[t[0]-1] == t[2])
        ans = max(ans, res)
    else:
        for a in range(A[-1] if A else 1, M + 1):
            A.append(a)
            dfs()
            A.pop()


dfs()
print(ans)
