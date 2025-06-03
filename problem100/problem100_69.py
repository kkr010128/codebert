import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline


X = int(input())
ans = min(8, 10-X//200)
print(ans)