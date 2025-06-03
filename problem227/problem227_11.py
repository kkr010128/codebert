import os, sys, re, math

(N, K) = [int(n) for n in input().split()]
H = [int(n) for n in input().split()]

H = sorted(H, reverse=True)[K:]
print(sum(H))
