N=int(input())
r=[0]*10000
for i in range(1,101):
    for j in range(1,101):
        for k in range(1,101):
            v = i*i + j*j + k*k + i*j + i*k + k*j
            if v <= 10000:
                r[v-1] += 1
for i in range(N):
    print(r[i])