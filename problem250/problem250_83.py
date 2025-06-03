import math


def resolve():
    import sys
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    # n = int(input().rstrip())
    x = int(input().rstrip())

    def get_sieve_of_eratosthenes(n: int):
        candidate = [i for i in range(2, n + 1)]

        primes = []
        while len(candidate) > 0:
            prime = candidate[0]
            candidate = [num for num in candidate if num % prime != 0]
            primes.append(prime)
        return primes

    # xまでの素数
    primes = get_sieve_of_eratosthenes(x)

    ans = x
    if not x in primes:
        while True:
            if any([ans % prime == 0 for prime in primes]):
                ans += 1
                continue
            break

    print(ans)




if __name__ == "__main__":
    resolve()
