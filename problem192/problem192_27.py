import sys
from collections import Counter

c = None

def resolve(in_, out):
    n = int(in_.readline())
    a = tuple(map(int, in_.readline().split()))

    c = dict(Counter(a))

    total = sum(v * (v - 1) // 2 for v in c.values())

    for ai in a:
        ans = total - (c[ai] - 1)
        print(ans, file=out)


def main():
    resolve(sys.stdin.buffer, sys.stdout)


if __name__ == '__main__':
    main()
