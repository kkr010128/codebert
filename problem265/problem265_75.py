n=int(input())
#m1,d1=map(int,input().split())
#hl=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
import math
flag=':('
for x in range(1,n+1):
    price=math.floor(x*1.08)
    if math.floor(x*1.08) == n:
        flag=x
        break
print(flag)