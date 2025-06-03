#時間の無駄なのでクソ問と割り切って飛ばす
def prod(array):
    res = 1
    for a, _ in array:
        res *= a
        res %= MOD
    return res

MOD = 10**9 + 7
N, K = map(int, input().split())
if N==K:
    res = 1
    for a in map(int, input().split()):
        res *= a
        res %= MOD
    print(res)
    exit()
A = []
allsgn = 0
for a in map(int, input().split()):
    A.append((abs(a), a < 0))
    allsgn += a<0
A.sort(reverse=True)
sgn = 0
s0 = -1
lastA = -1
for i, p in enumerate(A[:K]):
    a, s = p
    sgn += s
    if s != s0:
        lastA = i-1
    s0 = s
lasts = s0
if allsgn==N:
    if K%2==1:
        print((-prod(A[-K:]))%MOD)
        exit()
    else:
        print(prod(A[:K])%MOD)
        exit()
if sgn%2==0:
    print(prod(A[:K])%MOD)
    exit()
if lasts != A[K][1]:
    res = prod(A[:K-1])*A[K][0]
else:
    firstA = None
    for i, p in enumerate(A[K:],start=K):
        a, s = p
        if s != lasts:
            firstA = i
            break
    if lastA == -1 or (firstA is not None and A[K][0]/A[lastA][0] < A[firstA][0]/A[K-1][0]):
        res = prod(A[:K - 1]) * A[firstA][0]
    else:
        res = prod(A[:lastA]) * prod(A[lastA + 1:K + 1])
print(res%MOD)
"""
6 3
5 -3 -3 -3 -3 -2

10 7
-10 -10 -10 -10 10 10 10 10 10 10
"""
