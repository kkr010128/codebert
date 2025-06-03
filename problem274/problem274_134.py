import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, M = mapint()
S = list(input())

def solve():
    now = N
    choice = []
    while 1:
        if now==0:
            return choice[::-1]
        for m in range(M, 0, -1):
            nx = now-m
            if nx<0: continue
            if S[nx]=='1': continue
            now = nx
            choice.append(m)
            break
        else:
            return [-1]

print(*solve())