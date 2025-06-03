import os, sys, re, math

(N, K) = [int(n) for n in input().split()]
H = [int(n) for n in input().split()]

print(len(list(filter(lambda h: h >= K, H))))
