a, b, m = list(map(int, input().split()))
fridges = list(map(int, input().split()))
microwaves = list(map(int, input().split()))

price_min = min(fridges) + min(microwaves)
for _ in range(m):
	x, y, c = list(map(int, input().split()))
	price = fridges[x-1] + microwaves[y-1] - c
	if price < price_min:
		price_min = price
		
print(price_min)