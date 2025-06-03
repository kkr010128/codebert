import math

while True:
    n = int(raw_input())
    if n == 0:
        break
    s = map(int, raw_input().split())
    m = float(sum(s)) / n
    a2 = (sum(map(lambda x: (x-m)**2, s))) / n
    a = math.sqrt(a2)
    print("%f" % (a, ))