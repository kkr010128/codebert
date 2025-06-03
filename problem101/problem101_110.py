a, b, c = map(int, input().split())
k = int(input())

if a >= b:
    x = a // b
    x_ = len(bin(x)) - 2
else:
    x_ = 0

b *= 2 ** x_

if b >= c:
    y = b // c
    y_ = len(bin(y)) -2
else:
    y_ = 0

if (x_ + y_) <= k:
    print('Yes')
else:
    print('No')