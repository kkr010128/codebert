def gcds(*numbers):
    from math import gcd
    from functools import reduce
    return reduce(gcd, numbers)

def resolve():
    K = int(input())
    ans = 0
    import itertools
    for i, j, k in itertools.combinations_with_replacement(range(1, K+1), 3):
        l = len(set([i, j, k]))
        mu = 1
        if l == 3:
            mu = 6
        elif l == 2:
            mu = 3
        ans += gcds(i, j, k) * mu
    print(ans)

if '__main__' == __name__:
    resolve()