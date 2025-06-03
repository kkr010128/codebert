import math

while True:
    line = int(input())
    if line == 0:
        break
    l = [float(s) for s in input().split()]
    avg = sum(l) / len(l)
    a2 = 0
    for i in l:
        a2 += (avg - i) ** 2

    print(math.sqrt(a2 / len(l)))