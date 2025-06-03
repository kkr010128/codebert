N = int(input())
A = list(map(int,input().split()))

D = [0] * (10**6 + 1)
A.sort()
for i in range(N):
    D[A[i]] += 1
    
ans = 0
for i in range(1, 10**6+1):
    if D[i]:
        if D[i]==1:
            ans += 1
        for j in range(i,A[-1]+1,i):
            D[j] = 0
print(ans)