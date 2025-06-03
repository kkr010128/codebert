N = int(input())
L = [1]*(N+1)
for k in range(2,N+1):
    t = 1
    while k*t <= N:
        L[k*t] += 1
        t += 1
ans = 0
for k in range(1,N+1):
    ans += k*L[k]
print(ans)
