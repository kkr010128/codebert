n,d=map(int,input().split())
s=0
for _ in range(0,n):
    x,y=map(int,input().split())
    if (x**2+y**2)**0.5<=d:
        s=s+1
print(s)        
