def cal(i,j,k):
    a = i ** 2 + j ** 2 + k ** 2 + i * j + j * k + k * i 
    return a

N = int(input())
ans = [0] * (N + 1)
m = int(N ** 0.5)
for i in range(1,m):
    for j in range(1,m):
        for k in range(1,m):
            if cal(i,j,k) <= N:
                ans[cal(i,j,k)] += 1

for i in range(1,N+1):
    print(ans[i])