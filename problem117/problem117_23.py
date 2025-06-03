import math
import sys
import collections
import bisect
readline = sys.stdin.readline


def main():
    n, m, k = map(int, readline().rstrip().split())
    A = list(map(int, readline().rstrip().split()))
    B = list(map(int, readline().rstrip().split()))

    a, b = [0], [0]
    for i in range(n):
        a.append(a[i] + A[i])
    for i in range(m):
        b.append(b[i] + B[i])

    ans = 0
    j = m

    for i in range(n + 1):
        if a[i] > k:
            break
        while b[j] > k - a[i]:
            j -= 1
        ans = max(ans, i + j)

    print(ans)


if __name__ == '__main__':
    main()
