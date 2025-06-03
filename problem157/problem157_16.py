import collections
import sys
readline = sys.stdin.readline


def main():
    n = int(readline().rstrip())
    A = list(map(int, readline().rstrip().split()))
    ans = 0
    c = collections.Counter()

    for i in range(n):
        ans += c[i + 1 - A[i]]
        c[i + 1 + A[i]] += 1

    print(ans)


if __name__ == '__main__':
    main()
