N = int(input())
x = list(map(int,input().rstrip().split()))
ans = 0
for i in range(N):
    for j in range(i+1,N):
        ans+=x[i]*x[j]
print(ans)