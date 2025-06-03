import math

mod = 10**9+7
N = int(input())
'''
def modpow(x,y):
    res = 1
    for _ in range(y):
        res = res * x % mod
    return res
'''
def modpow(a,n):
    res = 1
    while n > 0:
        if n & 1:
            res = res *a % mod
        a = a * a % mod
        n >>= 1
    return res

def main():
    ans = 0
    x0 = modpow(8,N)
    x1 = modpow(9,N)
    x2 = modpow(10,N)
    ans = (x2-2*x1+x0)%mod    

    print(ans)
main()