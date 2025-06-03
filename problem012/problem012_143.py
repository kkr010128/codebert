import math

def checkPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    N = input()
    cnt = 0
    for i in range(N):
        n = input()
        if checkPrime(n):
            cnt += 1
    print cnt