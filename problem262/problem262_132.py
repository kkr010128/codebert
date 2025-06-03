import sys
import math
n=int(input())
A=[]
xy=[[]]*n
for i in range(n):
    a=int(input())
    A.append(a)
    xy[i]=[list(map(int,input().split())) for _ in range(a)]

ans=0

for bit in range(1<<n):
    tmp=0
    for i in range(n):
        if bit>>i & 1:
            cnt=0
            for elem in xy[i]:
                if elem[1]==1:
                    if bit>>(elem[0]-1) & 1:
                        cnt+=1
                else:
                    if not (bit>>(elem[0]-1) & 1):
                        cnt+=1
            if cnt==A[i]:
                tmp+=1
            else:
                continue
    
    if tmp==bin(bit).count("1"):
        ans=max(bin(bit).count("1"),ans)
print(ans)




