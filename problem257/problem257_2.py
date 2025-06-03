n=int(input())
l=list(map(int,input().split()))
c=1
s=0
for i in l:
    if(i==c):
        c+=1
    else:
        s+=1
if(s==n):
    print(-1)
else:
    print(s)