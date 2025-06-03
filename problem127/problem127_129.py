x, y = input().split()
x = int(x)
y = int(y)

if y % 2 == 0 and 2 * x <= y <= 4 * x:
    print('Yes')
else:
    print('No')