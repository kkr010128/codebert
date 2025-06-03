import sys
def input(): return sys.stdin.readline().strip()
def MAP(): return map(int, input().split())

n, a, b = MAP()
print(abs(a - b) // 2 if not (a - b) % 2 else abs(a - b) // 2 + min(min(a, b) - 1, n - max(a, b)) + 1)