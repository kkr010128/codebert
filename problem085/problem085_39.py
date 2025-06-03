import numpy as np
import sys
i4 = np.int32
i8 = np.int64
u4 = np.uint32

if sys.argv[-1] == 'ONLINE_JUDGE':
    from numba.pycc import CC
    from numba import njit
    from numba.types import int64, Array, uint32
    cc = CC('my_module')

    @cc.export('factorization', (uint32, ))
    @njit
    def factorization(N):
        p = np.zeros(N + 1, u4)
        n_max = int(np.sqrt(N)) + 1
        p[0] = 1
        p[1] = 1
        for i in range(2, n_max):
            if p[i] == 0:
                j = i
                while j <= N:
                    p[j] = i
                    j += i
        for i in range(n_max, N + 1):
            if p[i] == 0:
                p[i] = i
        return p

    @cc.export('solve', (Array(uint32, 1, 'C'),))
    def solve(A):
        a = np.sort(A)
        p_max = a[-1]
        p = factorization(p_max)
        primes_num = 0
        for i in range(p.shape[0]):
            if i == p[i]:
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
        stack = np.empty(20, u4)
        p_stack = 0
        for d in a:
            while d > 1:
                x = p[d]
                for i in range(p_stack):
                    if stack[i] == x:
                        break
                else:
                    stack[p_stack] = x
                    p_stack += 1
                d //= x

            while p_stack > 0:
                p_stack -= 1
                check[stack[p_stack]] += 1

        if check.max() > 1:
            return 1
        else:
            return 0
    cc.compile()
    from my_module import solve, factorization
    exit()

from my_module import solve, factorization

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


if __name__ == '__main__':
    main('/dev/stdin')