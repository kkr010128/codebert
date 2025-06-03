import math
import itertools
import sys
n,k = list(map(int,input().split()))
h = list(map(int,input().split()))

h.sort(reverse=True)
ans = 0
for i in range(len(h)):
    if(h[i] < k):
        ans = i
        print(ans) 
        sys.exit()

print(len(h))