import sys
sys.setrecursionlimit(4100000)
import math
INF = 10**9

def main():
    n = int(input())
    s,t = input().split()

    ans = ''
    for i in range(n):
        ans += s[i] + t[i]
    print(ans)


if __name__ == '__main__':
    main()
