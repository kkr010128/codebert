def is_prime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2

    return True


n = int(raw_input())
ans = 0

for i in range(n):
    x = int(raw_input())
    if (is_prime(x)):
        ans += 1

print ans