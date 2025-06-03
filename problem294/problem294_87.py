import itertools
 
n = int(input())
A = list(map(int,input().split()))
A.sort()
 
def binary_search(l,r,v):
    while r >= l:
        h = (l+r) // 2
        if A[h] < v:
            l = h+1
        else:
            r = h-1
    return r
 
ans = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        a = binary_search(j,n-1,A[i]+A[j])
        ans += a-j
 
print(ans)