from decimal import Decimal, getcontext
getcontext().prec = 10000


def f(x):
    return Decimal(x).sqrt()


a, b, c = map(int, input().split())
eps = Decimal(10) ** (-1000)
if f(a) + f(b) + eps < f(c):
    ans = "Yes"
else:
    ans = "No"

print(ans)
