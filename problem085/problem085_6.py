import sys
import numpy as np
i4 = np.int32
i8 = np.int64
u4 = np.uint32

if sys.argv[-1] == 'ONLINE_JUDGE':
    from numba.pycc import CC
    from numba import njit
    from numba.types import Array, int32, int64, uint32
    cc = CC('my_module')

    @njit
    def get_factorization(n):
        """
        nまでの割り切れる最小の素数を返す。
        """
        sieve_size = (n - 1) // 2
        sieve = np.zeros(sieve_size, u4)
        for i in range(sieve_size):
            if sieve[i] == 0:
                value_at_i = i*2 + 3
                for j in range(i, sieve_size, value_at_i):
                    if sieve[j] == 0:
                        sieve[j] = value_at_i
        return sieve


    @cc.export('solve', (Array(uint32, 1, 'C'),))
    @njit('(u4[::-1],)', cache=True)
    def solve(A):
        a = np.sort(A)
        p_max = a[-1]
        p = get_factorization(p_max)
        primes_num = 1
        for i in range(p.shape[0]):
            if i*2 + 3 == p[i]:
                primes_num += 1
        a_start = 0
        while a[a_start] == 1:
            a_start += 1
            if a_start == a.shape[0]:
                return 0
        a = a[a_start:]
        if len(a) > primes_num:
            return 1
        check = np.zeros(p_max + 1, u4)
        for d in a:
            if d & 1 == 0:
                check[2] += 1
                d //= 2
                while d & 1 == 0:
                    d //= 2
            prev = 2
            while d > 1:
                i = (d - 3) // 2
                f = p[i]
                if f > prev:
                    check[f] += 1
                    prev = f
                d //= f

        if check.max() > 1:
            return 1
        else:
            return 0

    cc.compile()
    exit(0)

else:
    from my_module import solve


def main(in_file):
    stdin = open(in_file)
    stdin.readline()
    A = np.fromstring(stdin.readline(), u4, sep=' ')
    ans = solve(A)
    if ans:
        g = np.gcd.reduce(A)
        if g > 1:
            ans = 2
        else:
            ans = 1
    p = ['pairwise coprime', 'setwise coprime', 'not coprime']
    print(p[ans])


main(0)
