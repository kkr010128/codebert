N,X,Y = map(int, input().split())
X,Y = X-1,Y-1

ans = [0] * N
for i in range(N):
    for j in range(i+1,N):
        dist = min(abs(i-j), abs(i-X) + 1 + abs(Y-j))
        ans[dist] += 1
print(*ans[1:], sep='\n')