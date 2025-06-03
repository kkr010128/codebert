X = int(input())

def is_prime(n):
    a = 2
    while a*a < n:
        if n%a == 0:
            return False
        a += 1
    return True
        

while True:
    if is_prime(X):
        break
    X += 1

print(X)