def abc177_e():
    n = int(input())
    A = [int(x) for x in input().split()]

    def prime_factorize(n:int)->set:
        ''' nの素因数分解 '''
        arr = []
        while n % 2 == 0:
            arr.append(2)
            n = n // 2
        f = 3
        while f*f <= n:
            if n%f == 0:
                arr.append(f)
                n = n // f
            else:
                f += 2
        if n != 1:
            arr.append(n)
        return set(arr)

    import math
    gcd_all = A[0]
    factors = [0]*(10**6 + 1)
    pairwise = True

    for ai in A:
        gcd_all = math.gcd(gcd_all, ai)
        for p in prime_factorize(ai):
            if factors[p]: pairwise = False
            factors[p] = 1

    if pairwise: ans = 'pairwise coprime'
    elif gcd_all == 1: ans = 'setwise coprime'
    else: ans = 'not coprime'
    print(ans)

if __name__ == '__main__':
    abc177_e()