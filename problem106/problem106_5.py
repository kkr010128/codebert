n = int(input())
ans = [0 for x in range(10001)]

for i in range(1, 100):
    for j in range(1, 100):
        for k in range(1, 100):
            v = i*i + j*j + k*k + i*j + i*k + j*k
            if v < 10001:
                ans[v] += 1
for i in range(n):
    print(ans[i+1])