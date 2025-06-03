import math

def isPrime(x):
    if(x == 1 ):
        return False

    n = int(math.sqrt(x))

    for i in range(2,n+1):
        if(x % i == 0):
            return False
    return True

n = int(input())
dataset = []
while (n > 0):
     dataset.append(int(input()))
     n -=1

prime_number = 0
for x in dataset:
    if(isPrime(x)):
        prime_number += 1

print(prime_number)