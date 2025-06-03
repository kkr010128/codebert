import sys
input = sys.stdin.readline
from bisect import *

def judge(x):
    cnt = 0
    
    for Ai in A:
        cnt += N-bisect_left(A, x-Ai+1)
    
    return cnt<M

def binary_search():
    l, r = 0, 2*max(A)
    
    while l<=r:
        m = (l+r)//2
        
        if judge(m):
            r = m-1
        else:
            l = m+1
    
    return l

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
border = binary_search()
acc = [0]*(N+1)

for i in range(N):
    acc[i+1] = acc[i]+A[i]
    
cnt = 0
ans = 0

for Ai in A:
    j = bisect_left(A, border-Ai+1)
    cnt += N-j
    ans += (N-j)*Ai+acc[N]-acc[j]

ans += (M-cnt)*border
print(ans)