import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, K = mapint()
mod = 10**9+7

ans = 0
for i in range(K, N+2):
    ans += (N+(N-i+1))*i//2-(i*(i-1)//2)+1
    ans %= mod
print(ans)