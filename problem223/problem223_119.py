import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
P = [int(x) for x in sys.stdin.readline().rstrip().split()]


# 目が 1 ... p のときの期待値
def kitaichi(p):
    return (p + 1) / 2

goukei = 0
for i in range(K):
    goukei += kitaichi(P[i])

gmax = goukei
for i in range(N - K):
    goukei = goukei + kitaichi(P[K + i]) - kitaichi(P[i])  # 次の区間の合計
    gmax = max(goukei, gmax)

print(gmax)
