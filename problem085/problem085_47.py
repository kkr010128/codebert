FAST_IO = 0
if FAST_IO:
    import io, sys, atexit
    rr = iter(sys.stdin.read().splitlines()).next
    sys.stdout = _OUTPUT_BUFFER = io.BytesIO()

    @atexit.register
    def write():
        sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
else:
    rr = raw_input
rri = lambda: int(rr())
rrm = lambda: map(int, rr().split())
rrmm = lambda n: [rrm() for _ in xrange(n)]

####
from collections import defaultdict as ddic, Counter, deque
import heapq, bisect, itertools
MOD = 10 ** 9 + 7

def solve(N, A):
    from fractions import gcd
    g  = A[0]
    for x in A:
        g=  gcd(g,x)
    if g > 1:
        return "not coprime"

    seen = set()
    for x in A:
        saw = set()
        while x % 2 == 0:
            x //= 2
            saw.add(2)
        d = 3
        while d*d <= x:
            while x%d == 0:
                saw.add(d)
                x //= d
            d += 2
        if x > 1:
            saw.add(x)

        for p in saw:
            if p in seen:
                return "setwise coprime"
        seen |= saw

    return "pairwise coprime"

N= rri()
A = rrm()

print solve(N, A)
