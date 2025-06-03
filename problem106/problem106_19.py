n=int(input())
a=[0]*(n+1)
d=0
for i in range(1,101):
    for j in range(1,101):
        for h in range(1,101):
            c=i**2+j**2+h**2+i*j+j*h+i*h
            if c<=n:
                a[c]+=1
for i in a[1:]:
    print(i)