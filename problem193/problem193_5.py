from collections import defaultdict
H,W,K = map(int,input().split())
S = [0] * H
for i in range(H):
    S[i] = input()

INF = H + W - 2

def bi(x):
    global H
    o = [0]*(H-1)
    i = 0
    while x != 0:
        o[i] = x % 2
        i += 1
        x //= 2
    return o

def hoge(n):
    global K
    b = bi(n)
    d = defaultdict(set)
    j = 0
    for i in range(H):
        d[j].add(i)
        if i == H - 1:
            break
        if b[i]:
            j += 1
    dlen = len(d)
    T = [0]*dlen
    for k,V in d.items():
        T[k] = [0]*W
        for i in range(W):
            for v in V:
                T[k][i] += int(S[v][i])
            if T[k][i] > K:
                return INF
    ans = dlen - 1
    U = [T[x][0] for x in range(dlen)]
    for i in range(1,W):
        flag = 0
        for k in range(dlen):
            U[k] += T[k][i]
            if U[k] > K:
                flag = 1
        if flag == 1:
            ans += 1
            for k in range(dlen):
                U[k] = T[k][i]
    return ans

ANS = INF
for i in range(2**(H-1)):
    ANS = min(ANS,hoge(i))

print(ANS)