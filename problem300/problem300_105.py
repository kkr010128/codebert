a,b=map(int,input().split())
c=1
for i in range(2,int(max(a**.5,b**.5))+2):
    if a%i==0==b%i:
        c+=1
    while a%i==0:
        a//=i
    while b%i==0:
        b//=i
if a==b!=1:
    c+=1
print(c)