import math

while True:
    try:
        a, b = [int(i) for i in input().split()]

        gcd = math.gcd(a, b)
        lcm = a * b // gcd

        print(f'{gcd} {lcm}')
    except EOFError:
        break

