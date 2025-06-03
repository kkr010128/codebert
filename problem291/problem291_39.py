import sys
sys.setrecursionlimit(4100000)
import math
INF = 10**9
import itertools

def main():
    a,b = map(int, input().split())

    print(max(0, a-2*b))


if __name__ == '__main__':
    main()
