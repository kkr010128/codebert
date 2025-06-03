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
MOD = 10**9 + 7
YES, NO, IMP = "YES", "NO", "IMPOSSIBLE"
from collections import defaultdict as ddic

N=rri()
A = rrmm(N)
X = []
Y = []
for x, y in A:
    X.append(x-y)
    Y.append(x+y)
#print X
#print Y

xlo, xhi = min(X), max(X)
ylo, yhi = min(Y), max(Y)

print(max(yhi-ylo, xhi-xlo))
