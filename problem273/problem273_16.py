import bisect

def solve(n, k, a):
    s = [0] * (n+1)
    for i in range(n):
        s[i+1] = s[i] + a[i]
    D = {}
    for i in range(n+1):
        p = (s[i] - i) % k
        if not p in D:
            D[p] = []
        D[p].append(i)
    res = 0
    for vs in D.values():
        m = len(vs)
        for j, vj in enumerate(vs):
            i = bisect.bisect_left(vs, vj+k) - 1
            res += i - j
    return res

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, k, a))