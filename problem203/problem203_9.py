a,b=map(int,input().split())
c=max(int(100*a/8),10*b)
d=min(int(100*a/8+100/8),10*b+10)
f=0
for x in range(c,d+1):
    if f==0 and int(x*0.08)==a and int(x*0.1)==b:
        f=1
        print(x)
if f==0:
    print(-1)

    
