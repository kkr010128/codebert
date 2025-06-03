X, Y = map(int, input().split(" "))
print(100000 * max(4 - X, 0) + 100000 * max(4 - Y, 0) + (400000 if X == 1 and Y == 1 else 0))