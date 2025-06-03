import sys
sys.setrecursionlimit(4100000)
import math
INF = 10**9

def main():
    n = int(input())
    S = input()

    if n%2 == 0:
        if S[:n//2] == S[n//2:]:
            print('Yes')
            return
    print('No')


if __name__ == '__main__':
    main()
