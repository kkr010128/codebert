n=int(input())
a=list(map(int,input().split()))
x=0
temp=1
f=False
for i in range(n):
    if a[i]==temp:
        f=True
        temp+=1
    else:
        x+=1
if f:
    print (x)
else:
    print (-1)