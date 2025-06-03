import math
while True:
    n = int(input())
    if n == 0: break
    s = list(map(int,input().split()))
    dis = 0
    mean = sum(s)
    mean /= n
    for s in s:
        dis += (s-mean)**2
    print('{0:.5f}'.format(math.sqrt(dis/n)))
    

