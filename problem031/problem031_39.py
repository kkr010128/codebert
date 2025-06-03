from math import sqrt
while 1:
    n = int(input())
    if n == 0:
        break
    a = list(map(int, input().split()))
    av = sum(a)/len(a)
    Sum = sum((x-av)**2 for x in a)
    print(f'{sqrt(Sum/n):.8f}')
