import math
while True:
    try:
        x, y = map(int, input().split())
        print(str(math.gcd(x,y)) + " " + str((x * y) // math.gcd(x, y)))
    except EOFError:
        break
