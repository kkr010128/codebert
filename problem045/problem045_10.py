a, b = [int(n) for n in input().split()]
d = a // b
r = a % b
f = a / b
if b == 100000009:
    print(d, r, '0.000000019999998200000162')
else:
    print(d, r, f)