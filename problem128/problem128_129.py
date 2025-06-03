# from sys import stdin
# input = stdin.readline
from collections import Counter

def solve():
    x,n = map(int,input().split())
    if n != 0:
        p = set(map(int,input().split()))
    if n == 0 or x not in p:
        print(x)
        return
    else:
        for i in range(100):
            if x - i not in p:
                print(x - i)
                return
            if x + i not in p:
                print(x + i)
                return


if __name__ == '__main__':
    solve()
