import math
while True:
    n = int(input())
    if n == 0:
        break

    s = [int(s) for s in input().split()]
    ave = sum(s) / n
    a = 0
    for N in s:
        a += (N - ave)**2
    
    a = math.sqrt((a / n))
    print(a)