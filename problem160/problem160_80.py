import itertools
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def score(A):
    res = 0
    for a, b, c, d in abcd:
        if A[b - 1] - A[a - 1] == c:
            res += d
    return res

  
def main(n, m, abcd):
    p = itertools.combinations_with_replacement(range(1, m+1), n)
    L = list(p)
    ans = 0
    for A in L:
        ans = max(ans, score(list(A)))
    return ans


n, m, q = map(int, readline().split())
abcd = [list(map(int, readline().split())) for _ in range(q)]

print(main(n, m, abcd))