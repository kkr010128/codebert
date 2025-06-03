#!/usr/bin/env python

from sys import stdin, stderr

def main():
   a, b, c = map(int, stdin.readline().split())

   print('Yes' if c-a-b >= 0 and 4*a*b < (c-a-b)**2 else 'No')

   return 0

if __name__ == '__main__': main()
