x, y = map(int, input().split())

prize = 0
if x <= 3:
    prize += (300000 - (x - 1) * 100000)
if y <= 3:
    prize += (300000 - (y - 1) * 100000)
if (x == 1) & (y == 1):
    prize += 400000
print(prize)