from functools import reduce
import fractions


def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)


def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)


def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


n = int(input())
a = list(map(int, input().split()))
l = lcm_list(a)
ans = sum([l // x for x in a]) % int(1e9+7)
print(ans)
