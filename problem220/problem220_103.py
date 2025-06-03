a,b=map(str,input().split())
c,d=map(int,input().split())
k=input()
if k==a:
    c-=1
else:
    d-=1
print(c,d)