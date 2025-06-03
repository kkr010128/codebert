import os, sys, re, math

(S, T) = [n for n in input().split()]
(A, B) = [int(n) for n in input().split()]
U = input()

if U == S:
    A -= 1
else:
    B -= 1

print('%s %s' % (A, B))
