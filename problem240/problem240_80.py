import sys
input = sys.stdin.readline
from collections import defaultdict


def main():
    N, M = map(int, input().split())
    passed = set([])
    penalty = defaultdict(int)
    for _ in range(M):
        p, S = input().split()
        if S == "WA" and p not in passed:
            penalty[p] += 1
        elif S == "AC":
            passed.add(p)
    ans = sum([penalty[p] for p in passed])
    print(len(passed), ans)


if __name__ == '__main__':
    main()
