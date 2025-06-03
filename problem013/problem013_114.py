n = int(input())
ns = []
max_profit = -1000000000
min_value = 1000000000
for i in range(n):
    num = int(input())
    if i > 0:
        max_profit = max(max_profit, num-min_value)
    min_value = min(num, min_value)
print(max_profit)
    
