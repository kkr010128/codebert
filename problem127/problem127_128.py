x,y=map(int,input().split())
r=0
for i in range(0,x+1):
    c=i
    t=x-c
    if c*2+t*4==y:
        r=r+1
if r!=0:
    print("Yes")
else:
    print("No")