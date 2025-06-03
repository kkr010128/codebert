def l_in(type_): return list(map(type_, input().split()))
def i_in(): return int(input())
def m_in(type_): return map(type_, input().split())
def r_in(n, type_): return [type_(input()) for _ in range(n)]
ans = None

def absmax(a, b):
    if abs(a) > abs(b): return a
    return b

def absmin(a, b):
    if abs(a) < abs(b): return a
    return b

a, b, c, d = m_in(int)
aa, bb, cc, dd = abs(a), abs(b), abs(c), abs(d)
x, y = 0, 0

abm = absmax(a, b)
cdm = absmax(c, d)
if (abm>0) == (cdm>0):
    ans = abm*cdm
else:
    abi = absmin(a, b)
    cdi = absmin(c, d)
    if (abi>0) == (cdm>0):
        k = abi*cdm
        if ans is None or k > ans: ans = k
    if (abm>0) == (cdi>0):
        k = abm*cdi
        if ans is None or k > ans: ans = k
    k = abi*cdi
    if ans is None: ans = k

print(ans)
