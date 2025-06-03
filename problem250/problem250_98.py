def is_prime(n):
    if n == 1:
        return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

x = int(input())
print(min(i for i in range(x, 100004) if is_prime(i)))