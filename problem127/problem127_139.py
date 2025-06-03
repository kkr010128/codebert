X, Y = map(int, input().split())
if Y % 2 == 1:
    print("No")
    exit(0)
if 0 <= 2 * X - Y / 2 <= X:
    print("Yes")
else:
    print("No")