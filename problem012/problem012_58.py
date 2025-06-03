import sys

def is_prime(x):
    if(x <= 3 and x > 1):
        return True
    elif(x % 2 == 0 or x % 3 == 0 or x < 2):
        return False
    i = 5
    while(i * i <= x):
        if(x % i == 0 or x % (i + 2) == 0):
            return False
        i += 6
    return True

l = []
count = 0
for input in sys.stdin:
    l.append(int(input))
for data in range(1,len(l)):
    if(is_prime(l[data]) == True):
        count += 1
print count
