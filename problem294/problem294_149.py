import bisect
n = int(input())
L = list(map(int,input().split()))

L.sort()
c=0
for i in range(n-2):
    ci=L[i]
    for j in range(i+1,n-1):
        cij = ci+L[j]
        c += bisect.bisect_left(L,cij,j+1,n)-j-1

print(c)
