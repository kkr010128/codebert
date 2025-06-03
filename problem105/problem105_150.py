import math
import sys
readline = sys.stdin.readline


def main():
    n = int(readline().rstrip())
    A = list(map(int, readline().rstrip().split()))
    cnt = 0
    for a in range(n):
        if ((a + 1) * A[a]) % 2 == 1:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
