def is_prime(n):
    for i in range(2,n):
        if i*i > n:
            return True
        if n%i == 0:
            return False
    return True
c = 0
n = int(input())
for _ in range(n):
    data = int(input())
    if is_prime(data): c+= 1
print(c)
