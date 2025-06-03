a, b, m = map(int, input().split())
list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))
total = min(list_a) + min(list_b)
for i in range(m):
    x, y, c = map(int, input().split())
    price = list_a[x - 1] + list_b[y - 1] - c
    total = min(price, total)
print(total)
