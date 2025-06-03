import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

K, X = map(int, input().split())

if 500 * K >= X:
    print('Yes')
else:
    print('No')