A, B, M = map(int, input().split())
lis_a = list(map(int, input().split()))
lis_b = list(map(int, input().split()))
lis_price = []

lis_price.append(min(lis_a) + min(lis_b))

for i in range(M):
    x, y, c = map(int,input().split())
    lis_price.append(lis_a[x-1] + lis_b[y-1] - c)

print(min(lis_price))
