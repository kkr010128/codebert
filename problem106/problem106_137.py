N=int(input())

Z=[0]*10005
for i in range(1,102):
    for j in range(1,102):
        for k in range(1,102):
            n=i**2+j**2+k**2+i*j+j*k+k*i
            if n<=N:
                Z[n-1]+=1
for i in range(N):
    print(Z[i])