import math

while True:
    a = int(input())
    if a == 0:
        break
    b = list(map(float, input().split()))
    m = sum(b)/a
    s = 0
    for i in range(int(a)):
        s += (b[i]-m)**2
    s = s / (int(a))
    s = math.sqrt(s)
    print(s)