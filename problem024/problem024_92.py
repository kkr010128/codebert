
def countPakages(P, k, W):
    i, n = 0, len(W)
    for j in range(k):
        s = 0
        while s + W[i] <=P:
            s += W[i]
            i += 1
            if i == n:
                return n
    return i

def ALDS1_4D():
    n_limit, k_limit, wi_limit = 100000, 100000, 10000
    n, k= map(int, input().split())
    W = [int(input()) for i in range(n)]
    Pleft, Pright = 0, n_limit * wi_limit
    while Pright - Pleft > 1:
        Pmid = (Pleft+Pright)//2
        v = countPakages(Pmid, k, W)
        if v < n:
            Pleft = Pmid
        else:
            Pright = Pmid

    return Pright
if __name__ == '__main__':
    print(ALDS1_4D())