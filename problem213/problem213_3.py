n = int(input())
X = sorted(list(map(int,input().split())))
ans = 10**10

for i in range(X[0],X[-1]+1):
    ans = min(ans, sum((i-x)**2 for x in X))

print(ans)