x = int(input())

h = x // 100
m = x % 100
if 0 <= m <= h * 5:
    print(1)
else:
    print(0)