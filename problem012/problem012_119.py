import math
def isPrime(number):
    for i in range(2,math.floor(math.sqrt(number))+1):
        if number%(i)==0:
            return False
    return True
N=int(input())
numbers=[]
for i in range(N):
    numbers.append(int(input()))
    pass
count=0
for number in numbers:
    if isPrime(number):
        count+=1
print(count)