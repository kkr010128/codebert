from math import tan, pi, degrees

a, b, x = map(int, input().split())

def solve(isOK):
    ng, ok = pi/2, 0
    while abs(ok-ng) > 10**-12:
        mid = (ng+ok) / 2
        if isOK(mid):
            ok = mid
        else:
            ng = mid
#    print('ok:', ok)
    print(degrees(ok))

def isOK1(theta):
    return a*a*tan(theta)/2 + x/a <= a*b
def isOK2(theta):
    return b*b/tan(theta)/2 >= x/a

if x/a >= a*b/2:
    solve(isOK1)
else:
    solve(isOK2)

