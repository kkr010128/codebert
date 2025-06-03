N, K = [int(i) for i in input().split()]
P = [int(i) for i in input().split()]
P2 = [(((P[i]+1)) / 2) for i in range(N)]
# i番目は1~P[i]の値を出す
# P[i]が大きいものからK個選んで期待値を求める
# 幅が最大のところを見つける
s = 0
init = 0
for i in range(K):
    s += P2[i] 
tmp = s
for i in range(1, N-K+1):
    tmp = tmp - P2[i-1] + P2[i+K-1]
    if s < tmp:
        s = tmp
        init = i

print(s)