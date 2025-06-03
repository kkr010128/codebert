import sys
input = sys.stdin.readline

(n, m), s = map(int, input().split()), sorted(list(map(int, input().split())), reverse = True)
print('Yes' if s[m-1] >= sum(s) / (m * 4) else 'No')