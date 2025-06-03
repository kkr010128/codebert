n, d = map(int, input().split())
cnt = 0

for i in range(n):
    Z = list(map(int, input().split()))
    X = Z[0]
    Y = Z[1]

    if X**2 + Y**2 <= d**2:
        cnt += 1
print(cnt)
