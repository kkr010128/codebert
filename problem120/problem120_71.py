n, k = map(int, input().split())
price = sorted(list(map(int, input().split())))

min_price = 0
for i in range(k) : 
    min_price += price[i]
    
print(min_price)