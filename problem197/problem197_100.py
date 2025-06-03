a, b, c = [int(_) for _ in input().split()]

if  a + b > c:
    print("No")
elif 4 * a * b < (c - b - a) ** 2:
    print("Yes")
else:
    print("No")
