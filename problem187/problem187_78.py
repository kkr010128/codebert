import sys
from collections import Counter


def main():
    input = sys.stdin.buffer.readline
    n, x, y = map(int, input().split())
    k_cnt = Counter()
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if i <= x:
                if j < y:
                    dist = min(j - i, (x - i) + 1 + (y - j))
                elif y <= j:
                    dist = (x - i) + 1 + (j - y)
            elif x < i < y:
                dist = min(j - i, (i - x) + 1 + abs(j - y))
            else:
                dist = j - i
            k_cnt[dist] += 1
    for i in range(1, n):
        print(k_cnt[i])


if __name__ == "__main__":
    main()
