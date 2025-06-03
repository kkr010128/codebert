#!/usr/bin/env python3

# from numba import njit
import sys
sys.setrecursionlimit(10**8)
# input = stdin.readline

# @njit
def solve(n,k,r,s,p,t):
  winHand = {"r":"p", "s":"b", "p":"s"}
  bestHandMemo = [""]*(n+1) # i手目の勝ち手
  
  memo = [-1]*(n+1)
  def calcPoint(char):
    if char == "r":
      return p
    elif char == "s":
      return r
    elif char == "p":
      return s
    else:
      raise ValueError
  def dp(i):
    if i == 0:
      return 0
    elif memo[i] != -1:
      return memo[i]
    elif i <= k:
      bestHandMemo[i-1] = winHand[t[i-1]] # 自由に出せる
      return dp(i-1) + calcPoint(t[i-1])
    elif winHand[t[i-1]] == bestHandMemo[i-k-1]:
      bestHandMemo[i-1] = "" # あいこでも負けても同じこと
      return dp(i-1)
    else: # 勝てる
      bestHandMemo[i-1] = winHand[t[i-1]]
      return dp(i-1) + calcPoint(t[i-1])
  
  for i in range(n+1):
    memo[i] = dp(i)

  return memo[n]
    



def main():
  N,K = map(int,input().split())
  R,S,P = map(int,input().split())
  T = input()
  print(solve(N,K,R,S,P,T))
  return

if __name__ == '__main__':
  main()
