import math

def prime(x):
    for i in range(2, int(math.sqrt(x))+1): 
        if x % i == 0:
            return False
    return True

n = int(raw_input())
a = []
for i in range(n):
    a.append(int(raw_input()))

num = 0
for i in range(n):
    if prime(a[i]):
        num += 1
print num