a=0
b=0
n=int(input())
for i in range(n):
    x=input().split()
    y=x[0]
    z=x[1]
    if y>z:a+=3
    elif y<z:b+=3
    else:
        a+=1
        b+=1
print(a,b)