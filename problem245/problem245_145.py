import os, sys, re, math

N = (int(input()))
S = input()

T = S.replace('ABC', '')
print((len(S) - len(T)) // 3)
