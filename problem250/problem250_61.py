import sys
import math

def isPrime(num):
    if num < 2: return False
    elif num == 2: return True
    elif num % 2 == 0: return False
    for i in range(3, math.floor(math.sqrt(num))+1, 2):
        if num % i == 0:
            return False
    return True

def callIsPrime(input_num):
    numbers = []
    for i in range(1, input_num):
        if isPrime(i):
            numbers.append(i)
    return numbers


def main():
    
    input = sys.stdin.readline
    x = int(input())
    primes = callIsPrime(x+1000)
    ans = [i for i in primes if i>=x]
    print(min(ans))


if __name__ == "__main__":
    main()

