mod = 10**9 + 7
_factorial = [1]
def fact(n):
    ''' n! % mod '''
    if n >= mod:
        return 0
    _size = len(_factorial)
    if _size < n+1:
        for i in range(_size, n+1):
            _factorial.append(_factorial[i-1]*i % mod)
    return _factorial[n]
    
_factorial_inv = [1]
def fact_inv(n):
    ''' n!^-1 % mod '''
    if n >= mod:
        raise ValueError('Modinv is not exist! arg={}'.format(n))
    _size = len(_factorial)
    if _size < n+1:
        for i in range(_size, n+1):
            _factorial.append(_factorial[i-1]*i % mod)
    _size_inv = len(_factorial_inv)
    if _size_inv < n+1:
        for i in range(_size_inv, n+1):
            _factorial_inv.append(modinv(_factorial[i]))
    return _factorial_inv[n]
    
def comb(n, r):
    ''' nCr % mod '''
    if r > n:
        return 0
    t = fact(n) * modinv(fact(n-r)) % mod
    t = t * modinv(fact(r)) % mod
    return t

def xgcd(a, b):
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0

def modinv(n):
    g, x, _ = xgcd(n, mod)
    if g != 1:
        raise ValueError('Modinv is not exist! arg={}'.format(n))
    return x % mod        

x, y = sorted(map(int, input().split()))
q, r = divmod(x+y, 3)
if r != 0:
    print(0)
else:
    print(comb(q, y-q))
