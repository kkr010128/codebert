import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8') 
inf = float('inf') ;mod = 10**9+7 
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n = int(input())
A = list(map(int, input().split()))
for i in range(n):
    if i == 0:
        max = A[i]
    else:
        if max > A[i]:
            ans += max - A[i]
        else:
            max = A[i]
print(ans)