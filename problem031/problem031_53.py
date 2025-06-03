import math
while True:
    n = int(input())
    if n == 0:
        break
    s = input().split(" ")
    t = list(map(int,s))
    goukei = 0
    for i in range(n):
        goukei += t[i]
    m = goukei / n
    sagoukei = 0
    for i in range(n):
        sagoukei += (t[i]-m)**2
    a = math.sqrt(sagoukei/n)
    print(a)