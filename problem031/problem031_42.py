from math import sqrt
from statistics import mean
while True:
    n = int(input())
    if n == 0:
        break
    else:
        L = list(map(int, input().split()))
        m = mean(L)
        temp = list(map(lambda x: (x-m)**2, L))
        SD = sqrt(sum(temp) / len(L))
        print(SD)
