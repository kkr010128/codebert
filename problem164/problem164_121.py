A,B,C,D=map(int,input().split())
ans=0
while 1:
    C-=B
    if C<=0:
        ans=1
        break
    A-=D
    if A<=0:
        break
if ans==1:
    print("Yes")
else:
    print("No")