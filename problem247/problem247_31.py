from fractions import gcd

def lcm(*args):
    ans = 1
    for x in args:
        ans = ans * x // gcd(ans, x)
    return ans

n, m = map(int, input().split())
a = [int(x) for x in input().split()]

def log(x):
    ans = 0
    while x % 2 == 0:
        ans += 1
        x //= 2
    return ans

def solve(a):
    tmp = None
    for ta in a:
        if tmp is None:
            tmp = log(ta)
        else:
            if tmp == log(ta):
                continue
            else:
                print(0)
                return
    l = lcm(*a)
    print(m // (l//2) - m // l)

solve(a)