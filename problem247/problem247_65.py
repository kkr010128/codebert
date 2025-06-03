
def gcd(a, b):
    while a != 0:
        b = b%a
        a, b = b, a
    return b

def lcm(a, b):
    return (a*b)//gcd(a,b)

n, m = map(int, input().split())

a = list(map(int, input().split()))

x = 1

for y in a:
    x = lcm(x, y//2)

for y in a:
    if (x//(y//2)) % 2 == 0:
        print(0)
        exit()

max_n = (m-x)//(2*x)

print(max_n+1)
