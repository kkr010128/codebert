import sys
input = sys.stdin.readline

K, X = map(int, input().split())
print('Yes' if X <= 500 * K else 'No')