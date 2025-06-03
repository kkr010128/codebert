N = int(input())
ans = [0]*(N+1)
for x in range(1,105):
    for y in range(1,105):
        for z in range(1,105):
            tmp = x**2 + y**2 + z**2 +x*y + y*z + z*x
            if tmp > N:
                continue
            ans[tmp]+=1
for i in range(1,N+1):
    print(ans[i])
