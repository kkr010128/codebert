def getDivisor(a,b,c):
    l = 0
    for i in range(a, b+1):
        if (c % i == 0):
            l += 1
    return l

a, b, c = map(int, input().split())
print(getDivisor(a,b,c))