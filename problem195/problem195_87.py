#!/usr/bin/python3
# -*- coding:utf-8 -*-

def main():
  k = int(input()) - 1
  li = '1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51'.split(', ')
  print(li[k])

if __name__=='__main__':
  main()

