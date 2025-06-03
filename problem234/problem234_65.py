import sys
import collections
import bisect


def main():
    n = int(input())
    ac, bc = collections.Counter([str(i + 1)[0] + str(i + 1)[-1] for i in range(
        n)]), collections.Counter([str(i + 1)[-1] + str(i + 1)[0] for i in range(n)])
    print(sum(ac[i] * bc[i] for i in ac.keys()))


if __name__ == '__main__':
    main()
