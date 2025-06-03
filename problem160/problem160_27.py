N, M, Q = map(int, input().split())
A, B, C, D = [],[],[],[]
for i in range(Q):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

L = []
def dfs(S):
    if len(S) == N:
        L.append(S)
    elif S == "":
        for i in range(M):
            S = str(i)
            dfs(S)
    else:
        for i in range(int(S[-1]), M):
            dfs(S+str(i))
dfs("")

Ans = 0
for l in L:
    ans = 0
    for a, b, c, d in zip(A,B,C,D):
        if int(l[b-1]) - int(l[a-1]) == c:
            ans += d
    Ans = max(ans, Ans)
print(Ans)
