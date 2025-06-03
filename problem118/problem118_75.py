N = int(input())
cum = [1]*2 + [2]*(N-1)
for i in range(2,N//2+1):
    for j in range(2*i,N+1,i):
        cum[j] += 1
ans = 0
for i in range(1,N+1):
    ans += i*cum[i]
print(ans)