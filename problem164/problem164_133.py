a,b,c,d=map(int,input().split())
for i in range(a, 0, -d):
    c=c-b 
    a=a-d 
if c<=0:
    print("Yes")
else:
    print("No")