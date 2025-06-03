N,*X = map(int, open(0).read().split())
ans = float('inf')
for i in range(1,max(X)+1):
    temp = 0
    for j in range(N):
        temp += (X[j]-i) ** 2
    ans = min(ans,temp)
print(ans)