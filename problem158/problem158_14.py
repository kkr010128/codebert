import math
k = int(input())
a, b = list(map(int, input().split()))
mul = math.floor(b/k) * k

if(mul >= a and (mul >= a and mul <= b)):
    print('OK')
else:
    print('NG')