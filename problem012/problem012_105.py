import math

def is_prime(x):
    if x == 2:
        return True

    if x % 2 == 0 or x < 2:
        return False

    i = 3
    x_sqrt = math.sqrt(x)
    while i <= x_sqrt:
        if x % i == 0:
            return False
        i += 2

    return True

if __name__ == "__main__":
    n = int(input())
    count = 0
    for i in range(n):
        if is_prime(int(input())):
            count += 1

    print(count)