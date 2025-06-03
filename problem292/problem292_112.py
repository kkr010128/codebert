import sys
sys.setrecursionlimit(4100000)
import math
INF = 10**9
import itertools

def main():
    n = int(input())
    D = list(map(int, input().split()))

    C = itertools.combinations(D, 2)
    ans = 0
    for c in C:
        ans += c[0]*c[1]

    print(ans)



if __name__ == '__main__':
    main()
