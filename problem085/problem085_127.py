MAX_A = 10**6 + 1
is_prim = [True] * MAX_A
is_prim[0] = is_prim[1] = False
for i in range(2, MAX_A):
    if not is_prim[i]: continue
    for j in range(i+i, MAX_A, i): is_prim[j] = False

def solve():
    C = [0] * MAX_A
    for a in A: C[a] += 1
    pairwise = True
    for p in [i for i in range(MAX_A) if is_prim[i]]:
        if sum(C[p::p]) > 1: pairwise = False
    if pairwise: return 'pairwise'
    from math import gcd
    g = 0
    for a in A: g = gcd(g, a)
    if g == 1: return 'setwise'
    return 'not'


n = int(input())
A = [*map(int, input().split())]
print(solve(), 'coprime')
