import sys
from collections import Counter
from itertools import combinations


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)

MOD = 10 ** 9 + 7
INF = float("inf")


def main():
    N = int(input())
    L = list(map(int, input().split()))
    count = Counter(L)
    key = count.keys()

    set_list = combinations(key, 3)
    answer = 0
    for s in set_list:
        a = s[0]
        b = s[1]
        c = s[2]
        if (a + b) > c and (b + c) > a and (c + a) > b:
            answer += count[a] * count[b] * count[c]
    print(answer)


if __name__ == "__main__":
    main()
