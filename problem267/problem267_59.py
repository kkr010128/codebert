import math
import sys
import collections
import bisect
readline = sys.stdin.readline


def main():
    n = int(readline().rstrip())
    s = readline().rstrip()
    cnt = 0
    for i in range(1000):
        x = str(i).zfill(3)
        a = s[:-1].find(x[0])
        if a != -1:
            b = s[a + 1: -1].find(x[1])
            if b != -1:
                c = s[a + b + 2:].find(x[2])
                if c != -1:
                    cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
