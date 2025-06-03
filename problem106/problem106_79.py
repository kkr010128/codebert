n=int(input())
m = int(n ** (0.5)) + 1
ans=[0]*(n+1)
for i in range(1,m):
    a=i**2
    for j in range(1,m):
        b=a
        b+=j**2+i*j
        for k in range(1,m):
            c=b
            c+=k**2+j*k+k*i
            if c<n+1:
                ans[c]+=1
for i in range(1,n+1):
    print(ans[i])