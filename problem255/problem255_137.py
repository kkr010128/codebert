"""
N = list(map(int,input().split()))
S = [str(input()) for _ in range(N)]
S = [list(map(int,list(input()))) for _ in range(h)] 
print(*S,sep="")
"""

import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()
inf = float("inf") # 無限

n = int(input())
s,t = input().split()

ans=""
for _ in range(n):
    ans+=s[_]+t[_]
print(ans)