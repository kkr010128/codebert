import math
def toRad(theta):
    return theta * math.pi / 180
def calc_S(_a, _b, _c):
    return (_a * _b * math.sin(toRad(_c))) / 2
def calc_L(_a, _b, _c):
    return _a + _b + math.sqrt(_a**2 + _b**2 - 2*a*b*math.cos(toRad(_c)))
def calc_H(_a, _b, _c):
    return _b * math.sin(toRad(_c))

a, b, c = map(int, input().split())
print(calc_S(a, b, c))
print(calc_L(a, b, c))
print(calc_H(a, b, c))