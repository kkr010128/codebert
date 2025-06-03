read = lambda: list(map(int, input().split()))

d, t, s = read()

if d / s > t:
    print("No")
else:
    print("Yes")