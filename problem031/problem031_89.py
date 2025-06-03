import math

while True:
    s = int(input())
    if s == 0:
        break

    r = list(map(float, input().split()))
    x = sum(r) / s
    sigtwo = sum(list(map(lambda y: (y-x)**2, r))) / s
    sig = math.sqrt(sigtwo)
    print("{:.8f}".format(sig))

