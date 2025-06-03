#!/usr/bin/python3
# -*- coding:utf-8 -*-

def main():
  h, w = map(int, input().split())
  grid = []
  for _ in range(h):
    grid.append(list(input().strip()))
  dp = [[0]*(w) for _ in range(h)]
  
  def cals_score(i, j):
    score = 10**9 + 7
    if i >= 1:
      score = dp[i-1][j] + (1 if grid[i-1][j]!=grid[i][j] else 0)
    if j >= 1:
      score = min(score, dp[i][j-1] + (1 if grid[i][j-1]!=grid[i][j] else 0))
    return score
      
  dp[0][0] = 1
  for i in range(1, w):
    dp[0][i] = cals_score(0, i)
  for i in range(1, h):
    dp[i][0] = cals_score(i, 0)

    
  for i in range(1, h):
    for j in range(1, w):
      dp[i][j] = cals_score(i, j)
  print(dp[-1][-1]//2 + dp[-1][-1]%2 * (grid[0][0]=='#'))

if __name__=='__main__':
  main()

