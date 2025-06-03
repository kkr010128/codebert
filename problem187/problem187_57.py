N, X, Y = map(int, input().split())

count = [0]*(N+1)
for i in range(1, N+1):
    for k in range(i+1, N+1):
        distik = min(k-i, abs(k-X) + abs(i - Y)+1, abs(k-Y) + abs(i-X)+1)
        count[distik] += 1

for i in range(1, N):
    print(count[i])
