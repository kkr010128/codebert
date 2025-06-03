def is_prime(x):
    if x <= 1:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

cnt = 0
for _ in range(int(input())):
    if is_prime(int(input())):
        cnt += 1
print(cnt)