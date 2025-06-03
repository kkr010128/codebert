a = list(map(int, input().split()))
b = (a[2] * 60 + a[3]) - (a[0] * 60 + a[1])
print(b - a[4])