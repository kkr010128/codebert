import math

def isprime(num):
    if num == 2:
        return True
    if num == 1 or num % 2 == 0:
        return False
    i = 3
    for i in range(3, math.floor(math.sqrt(num))+1, 2):
        if num % i == 0:
            return False
    return True


def count_prime_numbers(number_list):
    cnt = 0
    for target in number_list:
        if isprime(target):
            cnt += 1
    return cnt

N = int(input())
A = [int(input()) for i in range(N)]
print(count_prime_numbers(A))