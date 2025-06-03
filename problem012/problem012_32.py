def is_prime(num):
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


N = int(input())
num_list = [int(input()) for _ in range(N)]
print(sum(is_prime(num) for num in num_list))
