import math
while True:
    n = int(input())
    if n == 0:
        break
    L = list(map(float, input().split()))
    m = sum(L) / n
    Sum = 0
    for i in range(n):
        Sum = (L[i]-m)**2 + Sum
    a = math.sqrt(Sum / n)
    print(a)

