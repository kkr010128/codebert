x, y = input().split()
prizes = {'1': 300000, '2': 200000, '3': 100000}
ans = prizes.get(x, 0) + prizes.get(y, 0)
if x == y == '1':
    ans += 400000
print(ans)
