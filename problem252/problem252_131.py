import sys
from itertools import accumulate

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, M, *A = map(int, read().split())

    A.sort(reverse=True)

    counter = [0] * (A[0] + 1)
    for a in A:
        counter[a] += 1

    for i in range(A[0] - 1, -1, -1):
        counter[i] += counter[i + 1]

    def is_ok(x):
        c = 0
        for a in A:
            if x - a <= A[0]:
                c += counter[max(x - a, 0)]
            pass

        return c <= M

    ok = 2 * A[0] + 1
    ng = 2 * A[-1] - 1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid

    x = ok

    ans = 0
    csum = [0]
    csum.extend(accumulate(A))
    for a in A:
        if x - a <= A[0]:
            c = counter[max(x - a, 0)]
            ans += a * c + csum[c]
            M -= c

    ans += (x - 1) * M

    print(ans)

    return


if __name__ == '__main__':
    main()
