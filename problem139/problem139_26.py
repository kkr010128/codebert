a = list(map(int, input().split()))
kishou = a[0] * 60 + a[1]
shuusin = a[2] * 60 + a[3]
print(shuusin - kishou - a[4])