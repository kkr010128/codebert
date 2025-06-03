from math import ceil
a, b, c, d = map(int, input().split())
x = ceil(c/b)
y = ceil(a/d)
if x <= y:
    print('Yes')
else:
    print('No')