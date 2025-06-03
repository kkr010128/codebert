from bisect import bisect_left
X, N = list(map(int, input().split()))
P = list(map(int, input().split()))
P.sort()
S = set(P)

if N == 0:
    print(X)
    exit()


def bisectsearch_left(L, a):
    i = bisect_left(L, a)
    return(i)


k = bisectsearch_left(P, X)
if X != P[k]:
    print(X)
else:
    ct = 0
    while True:
        ct += 1
        if X-ct not in S:
            print(X-ct)
            break
        elif X+ct not in S:
            print(X+ct)
            break