import sys
input = lambda: sys.stdin.readline().rstrip()
input_nums = lambda: list(map(int, input().split()))

K, X = input_nums()

if 500*K >= X:
    print('Yes')
else:
    print('No')