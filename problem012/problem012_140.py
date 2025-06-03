from sys import stdin

def main():
    nums = [int(n) for n in stdin]

    primes = list(filter(is_prime, nums))
    print(len(primes))

def is_prime(n):
    if 1 == n:
        return False

    if 2 == n:
        return True

    if 0 == n % 2:
        return False

    for i in range(3, n, 2):
        if not i <= int(n/i):
            break

        if 0 == n % i:
            return False

    return True

if __name__ == '__main__':
    main()