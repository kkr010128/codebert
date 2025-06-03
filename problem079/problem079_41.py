import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

S = int(input())
mod = 10**9+7

pos = {0: 1}
neg = {0: 1}
for i in range(1, 10**4):
    pos[i] = (pos[i-1]*i)%mod
    neg[i] = pow(pos[i], mod-2, mod)

cnt = 1
ans = 0
while 3*cnt<=S:
    rest = S-3*cnt
    ans += pos[rest+cnt-1]*neg[rest]*neg[cnt-1]
    ans %= mod
    cnt += 1

print(ans)