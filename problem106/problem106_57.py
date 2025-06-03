n=int(input())
ans = [0 for _ in range(n+1)]
for i in range(1,int((n+1)**0.5)):
    for j in range(1,n+1):
        for k in range(1,n+1):
            v = i*i+j*j+k*k+i*j+j*k+k*i
            if v > n:
                break
            ans[v]+=1
for i in range(n):
    print(ans[i+1])