N,M,Q = map(int, input().split())
ab = tuple(tuple(map(int, input().split())) for _ in range(Q))
ans = 0
def dfs(A):
    global ans
    if len(A) == N:
        tmp = 0
        for i in range(Q):
            a,b,c,d = ab[i]
            if (A[b-1]-A[a-1]) == c:
                tmp += d
        if tmp > ans:
            ans = tmp


    else:
        last = A[-1] if len(A) > 0 else 1
        for i in range(last, M+1):
            A.append(i)
            dfs(A)
            A.pop()
dfs([])
print(ans)