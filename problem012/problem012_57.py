import math

def prime(x):
    if x == 2:
        return True
    elif x%2 == 0:
        return False
    else:
        i = 3
        while i <= math.sqrt(x):
           if x%i == 0:
                return False
           else:
                i += 2
        return True

        
        

p = 0
n = int(input())

for i in range(n):
    if prime(int(input())) == True:
        p += 1
        

print(p)