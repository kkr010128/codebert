a, b, c, d = map(int, input().split())
for i in range(101):
    x = c - b*i
    y = a - d*i
    if x <= 0:
        print("Yes")
        break
    elif y <= 0:
        print("No")
        break