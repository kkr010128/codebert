import os, sys, re, math, string

N = int(input())
S = input()

a = string.ascii_uppercase * 2
print(''.join([a[a.index(s) + (N % 26)] for s in S]))
