#!/usr/bin/python3
# -*- coding:utf-8 -*-

def main():
  n = int(input())
  la = list(map(int, input().strip().split()))
  la.sort(reverse=True)
  ans = sum(la[:(n+1)//2]) * 2 - la[0] - (la[(n+1)//2-1] if n%2==1 else 0)
  print(ans)

if __name__=='__main__':
  main()

