import math
while 1:
    n = int(input())
    if n == 0:
        break
    s = list(map(int,input().split()))
    m = sum(s) / len(s)
    x = 0
    for i in range(n):
        x += (s[i] -m )**2 / n
    a = math.sqrt(x)
    print(a)