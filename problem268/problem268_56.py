import sys
from collections import Counter as cc
def input(): return sys.stdin.readline().rstrip()
def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(mi())


def main():
    mod = 10**9 + 7
    n = ii()
    a = li()
    t = [0]*(n)
    ans = 1
    for i in range(n):
        if a[i] == 0:
            tmp = 3
        else:
            tmp = t[a[i]-1]
        ans *= tmp-t[a[i]]
        ans %= mod
        t[a[i]] += 1
    print(ans)


if __name__ == '__main__':
    main()