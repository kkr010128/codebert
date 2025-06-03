import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n,k = map(int, input().split())

m = n % k
m = 0 if m == 0 else abs(m - k)
print(min(n, m))
