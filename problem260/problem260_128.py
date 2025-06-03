import os, sys, re, math

A = [int(n) for n in input().split()]

print('win' if sum(A) <= 21 else 'bust')
