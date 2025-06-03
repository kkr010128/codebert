X, Y = map(int, input().split())
MD = pow(10, 9) + 7

def choose(n, a):
    x, y = 1, 1
    for i in range(a):
        x = x * (n - i) % MD
        y = y * (i + 1) % MD
    return x * pow(y, MD - 2, MD) % MD

a = (2*Y-X)//3
b = (Y-2*X)//-3
if a < 0 or b < 0 or (X+Y) % 3 != 0:
    print(0)
    exit()
print(choose(a+b, min(a,b)))