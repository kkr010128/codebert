# coding=utf-8
import itertools


def main():
    while True:
        n, t = map(int, raw_input().split())
        if n + t == 0:
            break
        print sum([1 if sum(three) == t else 0 for three in itertools.combinations(xrange(1, n+1), 3)])


if __name__ == '__main__':
    main()