import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

D = int(input())
C = list(map(int,input().split()))
S = [list(map(int,input().split())) for _ in range (D)]
t = [int(input()) for _ in range(D)]

M = 26
last = [0]*M
score = 0
for i in range(D):
    score += S[i][t[i]-1]
    last[t[i]-1] = i+1
    for m in range(M):
        score -= C[m]*(i+1-last[m])
    print(score)
