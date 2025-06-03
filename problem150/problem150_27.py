import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, K = mapint()
As = list(mapint())

dv = []
for _ in range(K.bit_length() + 1):
    l = [0] * N
    dv.append(l)

dv[0] = list(map(lambda x: x-1, As))

for k in range(1, K.bit_length() + 1):
    for n in range(N):
        dv[k][n] = dv[k - 1][dv[k - 1][n]]

a = []
for i in range(K.bit_length() + 1):
    if (K>>i)&1:
        a.append(i)

now = 0
for i in a:
    now = dv[i][now]
print(now+1)