n, k = map(int, input().split())

p = list(map(int,input().split()))

P = sorted(p)
price = 0
for i in range(k):
    price += P[i]

print(price)
