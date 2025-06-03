a, b, c = map(int, input().split())

x = c - b - a
if x > 0 and a * b * 4 < x * x:
	print("Yes")
else:
    print("No")