# coding: utf-8
# Your code here!
N=int(input())
A=list(map(int,input().split()))

if A[0]==1:
    if N==0:
        pass
    else:
        print(-1)
        exit()
elif A[0]>1:
    print(-1)
    exit()

limit=[1]

for a in A[1:]:
    limit.append(limit[-1]*2-a)

A=A[::-1]
limit=limit[::-1]

ans=A[0]
temp=A[0]


for i in range(len(limit)-1):
    a=limit[i+1]
    b=temp
    x=b-a
    y=a-x
    
    if x<0:
        x=0
        y=temp
    elif y<0:
        print(-1)
        exit()
    
    temp=x+y+A[i+1]
    ans+=temp
        

print(ans)