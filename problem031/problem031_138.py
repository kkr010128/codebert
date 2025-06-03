import math

foo = []
while True:
    n = int(input())
    if n == 0:
        break

    a = [int(x) for x in input().split()]
    
    ave = sum(a)/len(a)

    hoge = 0
    for i in a:
        hoge += (i - ave) ** 2
    hoge /= len(a)
    foo += [math.sqrt(hoge)]
for i in foo:
    print(i)