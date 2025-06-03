n, m, q = map(int,input().split())
a, b, c, d = [0] * q, [0] * q, [0] * q, [0] * q
for i in range(q):
    a[i], b[i], c[i], d[i] = map(int,input().split())

def score(l):
    res = 0
    for i in range(q):
        temp = l[b[i] - 1] - l[a[i] - 1]
        if temp == c[i]:res += d[i]

    return res

def dfs(l):
    global ans
    if len(l) == n:
        ans = max(ans, score(l))
        return #中で使われている関数の終了

    if l:
        temp = l[-1]
    else:
        temp = 1
    for v in range(temp, m + 1):
        l.append(v)
        dfs(l)
        l.pop()

ans = 0
dfs([])
print(ans)