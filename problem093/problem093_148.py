n, k = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))


def solve(start):
    loop = []
    llen = 0
    lsum = 0
    reach = [0]*n

    now = start
    while True:
        nxt = P[now]-1
        loop.append(now)
        llen += 1
        lsum += C[now]
        reach[now] = 1
        if reach[nxt]:
            break
        now = nxt
    
    if lsum <= 0 or llen >= k:
        res = -10 ** 20
        s = 0
        now = start
        for i in range(min(llen, k)):
            s += C[now]
            res = max(res, s)
            now = P[now]-1
        return res
    else:
        s = lsum * (k // llen)
        now = start
        for i in range(k % llen):
            s += C[now]
            now = P[now]-1
        j = loop.index(now)
        res = -10**20
        for i in range(llen):
            j -= 1
            res = max(res, s)
            s -= C[loop[j]]
        return res


def solver():
    ans = -10 ** 20
    for i in range(n):
        ans = max(ans, solve(i))
    return ans


print(solver())
