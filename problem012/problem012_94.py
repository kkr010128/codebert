def is_prime(x):
    if x == 2:
        return True
    elif x < 2 or x % 2 == 0:
        return False
    else:
        i = 3
        while i <= x ** 0.5:
            if x % i == 0:
                return False
            i += 2
    return True
 

n = int(input())
ret = 0
while n:
    x = int(input())
    if is_prime(x): ret += 1
    n -= 1

print(ret)