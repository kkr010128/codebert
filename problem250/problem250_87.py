N = int(input())

def prime_check(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

for x in range(N, 1000000):
    if prime_check(x):
        print(x)
        exit()