import os, sys, re, math

(K, X) = (int(n) for n in input().split())

if 500 * K >= X:
    print('Yes')
else:
    print('No')
