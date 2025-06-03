import bisect
from typing import List


def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(t(n, m, k, a, b))


def t(n: int, m: int, k: int, a: List[int], b: List[int]) -> int:
    aa = [0]
    for i in range(n):
        aa.append(aa[i] + a[i])
    bb = [0]
    for i in range(m):
        bb.append(bb[i] + b[i])

    ret = 0
    for i in range(n + 1):
        x = aa[i]
        s = k - x
        if s < 0:
            break
        j = bisect.bisect(bb, s) - 1
        ret = max(ret, i + j)

    return ret


if __name__ == '__main__':
    main()
