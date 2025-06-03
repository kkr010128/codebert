#!/usr/bin/env python

from sys import stdin, stderr

def main():
   K = int(stdin.readline())

   A = [1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51]

   print(A[K-1])

   return 0

if __name__ == '__main__': main()
