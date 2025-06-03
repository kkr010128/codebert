X, Y = map(int, input().split())
price = [0, 300000, 200000, 100000] + [0]*300
ans = price[X] + price[Y] + 400000*(X == Y == 1)

print(ans)