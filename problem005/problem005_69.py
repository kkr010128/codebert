import sys
dataset = sys.stdin.readlines()


def gcd(a, b):
    if b > a: return gcd(b, a)
    if a % b == 0: return b
    return gcd(b, a % b)

def lcd(a, b):
    return a * b // gcd(a, b)

for item in dataset:
    a, b = list(map(int, item.split()))
    print(gcd(a, b), lcd(a,b))