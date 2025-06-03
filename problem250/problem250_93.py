def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True

X = int(input())
while True:
    if isPrime(X):
        print(X)
        break
    X += 1