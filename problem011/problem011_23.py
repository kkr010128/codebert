#! python3
# greatest_common_divisor.py

def greatest_common_divisor(x, y):
    r = None

    if x >= y:
        r = x%y
        if r == 0: return y
    else:
        r = y%x
        if r == 0: return x

    return greatest_common_divisor(y, r)

x, y = [int(n) for n in input().split(' ')]
print(greatest_common_divisor(x, y))
