import sys
from collections import defaultdict

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    X, Y = map(int, readline().split())
    ans = 0
    if X==1:
        ans += 300000
    elif X==2:
        ans += 200000
    elif X==3:
        ans += 100000
    else:
        pass
    if Y==1:
        ans += 300000
    elif Y==2:
        ans += 200000
    elif Y==3:
        ans += 100000
    else:
        pass
    if X==Y==1:
        ans += 400000
    print(ans)


if __name__ == '__main__':
    main()
