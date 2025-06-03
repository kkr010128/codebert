n=int(input())
inp=list(map(int,input().split()))
from collections import Counter
z=0
k=1
for i in range(len(inp)):
    if inp[i]==k:
        z+=1
        k+=1
if z==0:
    print (-1)
else:
    print (len(inp)-z)
