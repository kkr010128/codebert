x,y=map(int,input().split())
n=0
for i in range(0,x+1):
    if 2*i+4*(x-i)==y:
        n=n+1
if n>0:
    print("Yes")
else:
    print("No")










