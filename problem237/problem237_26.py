n=int(input())
import bisect
L=[]
for i in range(n):
    x,l=map(int,input().split())
    a=x-l+0.1
    b=x+l-0.1
    L.append((b,a))
L=sorted(L)
rob=1
bottom=L[0][0]
for i in range(1,n):
    if L[i][1]>bottom:
        rob += 1
        bottom=L[i][0]
print(rob)