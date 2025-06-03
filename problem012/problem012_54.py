import math
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

def isprime(x):
    if x == 2:
        return True
    elif x % 2 == 0:
        return False
    i = 3
    while i <= math.sqrt(x):
        if x % i == 0:
            return False
        i += 2
    else:
        return True
   
counter = 0
for i in a:
    if isprime(i) == True:
        counter += 1
print(counter)