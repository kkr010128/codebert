N=int(input())
a=[0]*10**4
for j in range(1,101):
    for k in range(1,101):
        for h in range(1,101):
            tmp=h**2+j**2+k**2+h*j+j*k+k*h
            if tmp<=10000:
                a[tmp-1]+=1
for i in range(N):
    print(a[i])
