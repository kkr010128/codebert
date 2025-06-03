N, M, Q = map(int, input().split())
a, b, c, d = [0] * Q, [0] * Q, [0] * Q, [0] * Q
for i in range(Q):
    a[i], b[i], c[i], d[i] = map(int, input().split())

mx = 0

def dfs(Aary):
    global mx

    if len(Aary) == N + 1:
        scr = score(Q, Aary, a, b, c, d)
        if mx < scr:
            mx = scr
        return

    Aary.append(Aary[-1])
    while Aary[-1] <= M:
        dfs(Aary.copy())
        Aary[-1] += 1

def score(Q, A, a, b, c, d):
    ans = 0
    for i in range(Q):
        if A[b[i]] - A[a[i]] == c[i]:
            ans += d[i]

    return ans

dfs( [1] )

print(mx)
