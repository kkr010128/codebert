import math
n = int(input())
while (n != 0):
    nlist = list(map(float, input().split()))
    sum = 0
    for i in range(n):
        sum += nlist[i]
    aver = sum/n
    var = 0
    for i in range(n):
        var += (nlist[i] - aver)**2 / n
    dev = math.sqrt(var)
    print(dev)
    n = int(input())
