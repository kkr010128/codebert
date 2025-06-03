def canLoad(n, k, p):
    global w
    load = 0
    for i in range(n):
        load += w[i]
        if load <= p:
            continue
        k -= 1
        if k == 0:
            return False
        load = w[i]
    return True

def solve(n, k, pmin, pmax):
    if pmin + 1 >= pmax:
        return pmax
    newp = (pmax + pmin) // 2
    if canLoad(n, k, newp):
        return solve(n, k, pmin, newp)
    else:
        return solve(n, k, newp, pmax)

n, k = map(int, input().split())
w = [0]*n
wsum = 0
wmax = 0
for i in range(n):
    w[i] = int(input())
    wsum += w[i]
    if w[i] > wmax:
        wmax = w[i]

# p の最小の候補は wmax と ceil(wsum/k) の最大値
pmin = max(wmax, wsum // k if wsum % k == 0 else wsum // k + 1)
pmax = wsum
p = pmin
if not canLoad(n, k, pmin):
    p = solve(n, k, pmin, pmax)
print(p)

