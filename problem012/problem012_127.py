import sys
import math

def is_prime(x):
    if x == 2:
        return True

    if (x == 1) or (x % 2 == 0):
        return False

    for i in range(3, math.ceil(math.sqrt(x))+1, 2):
        if x % i == 0:
            return False

    return True
    
if __name__ == '__main__':
    element_number = int(input())

    output = 0
    for x in map(int, sys.stdin.readlines()):
        if(is_prime(x)):
            output += 1

    print(output)