# -*- coding: utf-8 -*-
import sys
from collections import Counter
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N = int(readline())
A = list(map(int,readline().split()))
cnt = Counter(A)
sum = 0
for n in cnt.values():
    sum += n*(n-1)//2
for a in A:
    print(sum-cnt[a]+1)