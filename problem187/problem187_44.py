N, X, Y = map(int, input().split())
d = Y-X+1
l = [0]*(N+1)
for i in range(1, N+1):
    for j in range(i, N+1):
        m = min(j-i, abs(X-i)+1+abs(Y - j))
        l[m] += 1
print(*l[1:-1], sep="\n")
