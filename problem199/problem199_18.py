#!/usr/bin/env python

from sys import stdin, stderr

def main():
   S = stdin.readline().strip()
   if (len(S) % 2) != 0:
      print('No')
      return 0
   for i in xrange(0, len(S), 2):
      if S[i:i+2] != 'hi':
         print('No')
         return 0
   print('Yes')

   return 0

if __name__ == '__main__': main()
