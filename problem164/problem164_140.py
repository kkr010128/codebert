A,B,C,D=map(int,input().split())
t=0
a=0
while A>0:
    A-=D
    t+=1
while C>0:
    C-=B
    a+=1
if t>=a:
    print('Yes')
else:
    print('No')