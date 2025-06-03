import math

def isprime(x):
        if x == 2:
                return True
        if x < 2 or x % 2 == 0:
                return False
        i = 3
        while(i <= math.sqrt(x)):
                if x % i == 0:
                        return False
                i += 2

        return True

num = raw_input()

count = 0
for i in range(int(num)):
        x = raw_input()
        if isprime(int(x)):
                count += 1

print count