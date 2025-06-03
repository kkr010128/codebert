import sys
input = sys.stdin.readline

a, b, k = map(int, input().split())
print(f'{a - k} {b}' if a >= k else (f'0 {b - (k - a)}' if a + b >= k else '0 0'))