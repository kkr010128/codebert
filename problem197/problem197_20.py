
A, B, C = map(int, input().split())

x = A * B * 4
y = (C - A - B) ** 2
if x < y and C - A - B > 0:
    print("Yes")
else:
    print("No")
