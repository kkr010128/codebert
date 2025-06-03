import sys
import itertools

sys.setrecursionlimit(10 ** 8)
ni = lambda: int(sys.stdin.readline())
nm = lambda: map(int, sys.stdin.readline().split())
nl = lambda: list(nm())
ns = lambda: sys.stdin.readline().rstrip()
dbg = lambda *args, **kwargs: print(*args, **kwargs, file=sys.stderr)

N = ni()
A = nl()
assert len(A) == (N + 1)


def solve():
    ar = list(itertools.accumulate(A[::-1]))
    ar.reverse()
    ar.append(0)
    assert len(ar) == (N + 2)
    if N == 0:
        return 1 if A[0] == 1 else -1
    if A[0] != 0:
        return -1
    inn = ans = 1
    for i in range(1, N + 1):
        b = 2 * inn - A[i]
        if b < 0:
            return -1
        inn = min(b, ar[i + 1])
        ans += inn + A[i]
    return ans


print(solve())
