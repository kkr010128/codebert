n=int(input())
l=[0]*(n+1)
for i in range(1,101):
    for j in range(1,101):
        for k in range(1,101):
            s=i**2+j**2+k**2+i*k+i*j+j*k
            if(s<=n):
                l[s]+=1
for i in range(1,n+1):
    print(l[i])
