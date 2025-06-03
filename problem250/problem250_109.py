X = int(input())

def is_prime(n):
    if n == 2: return True
    if n < 2 or n%2 == 0: return False
    m = 3
    while m*m <= n:
        if n%m == 0: return False
        m += 2
    return True

while 1:
    if is_prime(X):
        print(X)
        exit()
    X += 1