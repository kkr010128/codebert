#!/usr/bin/python3

import sys

def input():
    return sys.stdin.readline().rstrip('\n')

#S = input()
A1,A2,A3 = list(map(int,input().split()))

if A1+A2+A3 < 22:
    print('win')
else:
    print('bust')
