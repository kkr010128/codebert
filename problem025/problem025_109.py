import sys
from sys import stdin
input = stdin.readline

n = int(input())
A =[int(x) for x in input().split()]
q = int(input())
M =[int(x) for x in input().split()]

dp = [[-1 for i in range(2001)] for j in range(21)]

def solve(i,m):
    if dp[i][m] != -1:
        return dp[i][m]
    if m == 0:
        dp[i][m] = True
    elif i >= n:
        dp[i][m] = False
    elif solve(i+1,m):
        dp[i][m] = True
    elif solve (i+1, m-A[i]):
        dp[i][m] = True
    else:
        dp[i][m] = False
    return dp[i][m]

for m in M:
    if solve(0,m):
        print("yes")
    else:
        print("no")
