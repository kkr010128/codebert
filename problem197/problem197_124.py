from decimal import Decimal

a,b,c = map(int, input().split())
def convert(x):
    return Decimal(str(x)).sqrt()

if convert(a) + convert(b) < convert(c):
    print('Yes')
else:
    print('No')