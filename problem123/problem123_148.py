#!/usr/bin/python3
# -*- coding:utf-8 -*-

from functools import reduce

def main():
  n = int(input())
  la = list(map(int, input().strip().split()))
  x = reduce(lambda x, y: x ^ y, la)
  print(' '.join([str(x ^ a) for a in la]))

if __name__=='__main__':
  main()
