import sys

sys.setrecursionlimit(1000000)
input = lambda: sys.stdin.readline().rstrip()

K, X = map(int, input().split())
if K * 500 >= X:
    print("Yes")
else:
    print("No")