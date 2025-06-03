n = input()
x = map(int, input().split())
y = map(int, input().split())

x_y = [abs(xi - yi) for xi, yi in zip(x, y)]
for p in range(1, 4):
    print(sum(i ** p for i in x_y) ** (1 / p))
print(max(x_y))