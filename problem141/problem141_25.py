import sys

def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
sys.setrecursionlimit(10 ** 9)
INF = 10 ** 19
MOD = 10 ** 9 + 7

N = INT()
A = LIST()

if N == 0:
    if A[0] == 1:
        print(1)
    else:
        print(-1)
    exit()

cond1 = [0] * (N+1)
cond1[N] = A[N]
for i in range(N-1, -1, -1):
    cond1[i] = cond1[i+1] + A[i]

if min(cond1) <= 0:
    print(-1)
    exit()

cond2 = [0] * (N+1)
cond2[0] = 1
for i in range(1, N+1):
    cond2[i] = min(cond1[i], (cond2[i-1]-A[i-1]) * 2)

if min(cond2) <= 0:
    print(-1)
    exit()

if cond2[N] < A[N]:
    print(-1)
    exit()

ans = sum(cond2)
print(ans)
