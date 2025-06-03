n=int(input())
ch=0
curr=0
for i in range (n):
    a,b=map(int,input().split())
    if a==b:
        curr+=1
    else:
        curr=0
    if curr>=3:
        ch=1
if ch:
    print("Yes")
else:
    print("No")