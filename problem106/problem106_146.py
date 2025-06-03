n = int(input())
ans = [0] * (10**4 + 1)

for i in range(1,105):
    for j in range(1,105):
        for k in range(1,105):
            v = i*i+j*j+k*k+i*j+j*k+k*i
            if v < 10001:
                ans[v]+=1

for i in range(n):
    print(ans[i+1])
