import math

A, B = list(map(int, input().split()))
count = 0

def divisor(x):
    divs = []
    for i in range(1, math.floor(math.sqrt(x))+1):
        if x%i == 0:
            divs.append(i)
            if i**2 != x:
                divs.append(x//i)
    return divs

def evPrimal(x):
    if x < 4:
        return True
    divs = []
    for i in range(2, math.floor(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True

codiv = set(divisor(A)) & set(divisor(B))

for i in codiv:
    if evPrimal(i):
        count += 1

print(count)