a=int(input())
d=0
for i in range(2,int(a**0.5)+1):
    c=0
    while a%i==0:
        c+=1
        a//=i
    for i in range(1,60):
        if c>=i:
            c-=i
            d+=1
        else:
            break
    if a==1:
        break
if a!=1:
    d+=1
print(d)