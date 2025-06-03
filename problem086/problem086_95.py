a, b, c = map(int, input().split())

if a % b == 0:
    print(a//b * c)
else:
    print((a//b + 1) * c)