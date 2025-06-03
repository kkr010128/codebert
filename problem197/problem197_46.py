#!/usr/bin/env python3

# from numba import njit

# input = stdin.readline

# @njit
def solve(a,b,c):
  return c-a-b >= 0 and pow(c-a-b,2) > 4*a*b



def main():
  a,b,c = map(int,input().split())
  print("Yes" if solve(a,b,c) else "No")
  return

if __name__ == '__main__':
  main()
