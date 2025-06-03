import sys
import collections
import bisect
readline = sys.stdin.readline


def main():
    n = int(readline().rstrip())
    aList = sorted(list(map(int, readline().rstrip().split())))
    z = [0] * n
    for a in aList:
        z[a-1] += 1

    for i in range(n):
        print(z[i])


if __name__ == '__main__':
    main()
