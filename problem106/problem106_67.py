N = int(input())
ans = [0] * N
for i in range(1, 101):
    for j in range(1, 101):
        for k in range(1, 101):
            tmp = i**2+j**2+k**2+i*j+j*k+k*i
            if tmp <= N:
                ans[tmp-1] += 1
print(*ans, sep='\n')