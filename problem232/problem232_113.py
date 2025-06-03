a = list(map(int, input().split()))
x = 0
y = 0
for i in range(0,a[1]):
    x = x + a[0]*(10**i)
for i in range(0,a[0]):
    y = y + a[1]*(10**i)
if x<=y:
    print(y)
else:
    print(x)