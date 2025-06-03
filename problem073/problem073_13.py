from collections import defaultdict
from operator import mul
from functools import reduce


def main():
    n = int(input())
    p = [1] * (n + 1)
    for i in range(2, n + 1):
        if p[i] != 1:
            continue
        for j in range(i, n + 1, i):
            if p[j] == 1:
                p[j] = i
    ans = 1
    for i in range(2, n):
        m = i
        k = defaultdict(int)
        while m > p[m]:
            k[p[m]] += 1
            m //= p[m]
        k[m] += 1
        ans += reduce(mul, [e + 1 for e in k.values()])
    print(ans)


if __name__ == '__main__':
    main()
