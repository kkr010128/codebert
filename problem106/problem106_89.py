import math
n=int(input())
num=int(math.sqrt(n))
ans=[0]*(n+1)
for i in range(1,num+1):
    for j in range(1,num+1):
        for k in range(1,num+1):
            v=i*i+j*j+k*k+i*j+i*k+j*k
            if v<=n:
                ans[v]+=1
for i in range(n):
    print(ans[i+1])