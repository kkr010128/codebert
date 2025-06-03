import math
def isPrime(a):
    mx = math.sqrt(a)
    tmp = 2
    while tmp <= mx:
        if a % tmp == 0:
            return False
        tmp += 1
    return True

x = int(input())
tmp = 0
while True:
    if isPrime(x + tmp):
        f = 1
        print(x+tmp)
        break
    tmp += 1
