N, X, Y = map(int, input().split())

X -= 1
Y -= 1

ans = [0]*(N-1)
for i in range(N):
    for j in range(i+1, N):
        if i == j:
            continue
        cnt = min(abs(i-j), abs(X-i)+abs(j-Y)+1, abs(j-X)+abs(Y-i)+1)
        ans[cnt-1] += 1

for i in range(N-1):
    print(ans[i])
