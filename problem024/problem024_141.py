from sys import stdin
N, K = [int(_) for _ in stdin.readline().rstrip().split()]
W = [int(stdin.readline().rstrip()) for _ in range(N)]

def check(P):
    i = 0
    for _ in range(K):
        s = 0
        while s+W[i] <= P:
            s += W[i]
            i += 1
            if i == N:
                return N
    return i

def solver():
    mid, l, u = 0, 0, 100000*10000
    while u-l > 1:
        mid = (l+u)//2
        v = check(mid)
        if v >= N:
            u = mid
        else:
            l = mid
    return u
    
print(solver())
