from functools import reduce
import sys

N, M = map(int, input().split())
A = list(map(int, input().split()))


def lcm(a,b):
    return int(a * b / gcd(a, b))

def gcd(a, b):
    import fractions
    return fractions.gcd(a, b)


def temp(a):
    return int(a * 0.5)

max_a = max(A)

i = 0
while True:
    num = int((i+0.5) * max_a)
    if num > M:
        print(0)
        sys.exit()

    found = True
    for a in A:
        if int(num - 0.5 * a) % a != 0:
            found = False
            break
    if found:
        ans = 1
        break
    i += 1

aa = reduce(lcm, A)

ans += (M - num) // aa

print(int(ans))
