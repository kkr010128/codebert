import fractions
def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)
x=int(input())
y=lcm(x,360)
print(y//x)