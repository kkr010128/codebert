#!python3

import sys
iim = lambda: map(int, sys.stdin.readline().rstrip().split())

def resolve():
    N = int(sys.stdin.readline())
    N1 = N - 1

    ans = 0
    for i in range(1, N):
        ans += N1//i
    print(ans)
if __name__ == "__main__":
    resolve()
