import sys

# 最大公約数(greatest common divisor)を求める関数
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 最小公倍数(least common multiple)を求める関数
# //は切り捨て除算
def lcm(a, b):
    return a * b // gcd(a, b)

lines = sys.stdin.readlines()
for line in lines:
    a = list(map(int, line.split(" ")))
    print(gcd(a[0], a[1]), lcm(a[0], a[1]))

