import sys
import collections
import bisect


def main():
    n = int(input())
    a = [str(i + 1)[0] + str(i + 1)[-1] for i in range(n)]
    b = [str(i + 1)[-1] + str(i + 1)[0] for i in range(n)]
    ac, bc = collections.Counter(a), collections.Counter(b)
    print(sum(ac[i] * bc[i] for i in ac.keys()))


if __name__ == '__main__':
    main()
