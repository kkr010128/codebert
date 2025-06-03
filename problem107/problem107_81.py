def popcount(n):
    ret = 0
    while n > 0:
        ret += n & 1
        n >>= 1
    return ret

def f(n):
    ret = 0
    while n > 0:
        n %= popcount(n)
        ret += 1
    return ret

def mod(x, d):
    '''
    x % d where x: string, d: int
    '''
    rem = 0
    for i in range(len(x)):
        divd = (rem << 1) + int(x[i], 2)
        rem = divd % d

    return rem

N = int(input())
X = input()

popx = X.count('1')
qp = mod(X, popx + 1)  # X mod (popcount(X) + 1)
if popx - 1 > 0:
    qm = mod(X, popx - 1)   # X mod (popcount(X) - 1)

ans = []
pow2p = pow2m = 1
for i in range(N):
    if X[N - 1 - i] == '1':
        if popx == 1: # X_iが0
            ans.append(0)
        else:
            next = (qm - pow2m) % (popx - 1)
            ans.append(1 + f(next))
    else:  #  X[N - 1 - i] == '0'
        next = (qp + pow2p) % (popx + 1)
        ans.append(1 + f(next))

    pow2p = pow2p * 2 % (popx + 1)
    if popx > 1:
        pow2m = pow2m * 2 % (popx - 1)

for i in range(N - 1, -1, -1):
    print(ans[i])