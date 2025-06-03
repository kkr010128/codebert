import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

mod = 998244353
N, M, K = mapint()

pos = {}
neg = {}
pos[0] = 1
neg[0] = 1
for i in range(1, N+1):
    pos[i] = i*pos[i-1]%mod
    neg[i] = pow(pos[i], mod-2, mod)
ans = 0
for i in range(K+1):
    ans += M*pow((M-1), (N-i-1), mod)*pos[N-1]*neg[i]*neg[N-i-1]
    ans %= mod
print(ans)