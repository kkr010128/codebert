n, k = map(int, input().split())
p = list(map(int, input().split()))
sortPrice = sorted(p)
# print(sortPrice)
price = []
for i in range(0, k):
    price.append(sortPrice[i])
print(sum(price))