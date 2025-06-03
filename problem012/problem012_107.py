def isPrime(n):
    if (n == 1): return False
    if (n == 2): return True
    if (0 == n % 2) : return False
    i = 2
    while(n >= i * i):
        if (0 == n % i): return False
        i += 1
    return True

def main():
    c = 0
    n = input()
    for i in range(n):
        if (isPrime(input())):
            c += 1
    print(c)

main()