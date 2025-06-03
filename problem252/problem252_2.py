import sys
input = sys.stdin.readline
from bisect import *

def judge(x):
    cnt = 0
    
    for i in range(N):
        idx = bisect_left(A, x-A[i])
        cnt += N-idx
    
    return cnt>=M
    
def binary_search():
    l, r = 0, 10**11
    
    while l<=r:
        mid = (l+r)//2
        
        if judge(mid):
            l = mid+1
        else:
            r = mid-1
    
    return r

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
border = binary_search()
acc = [0]

for Ai in A:
    acc.append(acc[-1]+Ai)

ans = 0
cnt = 0

for i in range(N):
    idx = bisect_left(A, border-A[i]+1)
    ans += A[i]*(N-idx)+acc[N]-acc[idx]
    cnt += N-idx

ans += (M-cnt)*border

print(ans)