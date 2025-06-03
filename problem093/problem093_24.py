import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
def resolve():
    n, k = map(int, input().split())
    P = list(map(lambda x : int(x) - 1, input().split()))
    C = list(map(int, input().split()))

    # doubling table
    nexts = [P]
    vals = [C]
    totals = [C]
    for _ in range(60):
        next, val, total = nexts[-1], vals[-1], totals[-1]
        nnext, nval, ntotal = [0] * n, [0] * n, [0] * n
        for i in range(n):
            nnext[i] = next[next[i]]
            nval[i] = val[i] + val[next[i]]
            ntotal[i] = max(total[i], val[i] + total[next[i]])
        nexts.append(nnext)
        vals.append(nval)
        totals.append(ntotal)

    # answer
    ans = -INF
    for now in range(n):
        score = 0
        for d in range(59, -1, -1):
            if k >> d & 1:
                ans = max(ans, score + totals[d][now])
                score += vals[d][now]
                now = nexts[d][now]
    print(ans)
resolve()