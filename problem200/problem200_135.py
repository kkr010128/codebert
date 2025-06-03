a, b, m = map(int, input().split())
a_p = list(map(int, input().split()))
b_p = list(map(int, input().split()))

min_price = min(a_p) + min(b_p)

for i in range(m):
    x, y, c = map(int, input().split())
    min_price = min(min_price, a_p[x-1] + b_p[y-1] - c)
print(min_price)