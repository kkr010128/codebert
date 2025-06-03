import os, sys, re, math

(A, B) = [int(n) for n in input().split()]

print(max(A - B * 2, 0))
