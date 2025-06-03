from fractions import gcd
def lcm(x, y):
    return (x * y) // gcd(x, y)
def main():
    a,b = map(int,input().split())
    print(lcm(a, b))
main()
