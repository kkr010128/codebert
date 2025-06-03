import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    X = int(readline())

    def enum_primes(n):
        flag_num = (n + 1) // 2
        prime_flag = [True] * flag_num

        for num in range(3, int(n ** 0.5) + 1, 2):
            idx = (num - 1) // 2 - 1
            if prime_flag[idx]:
                for j in range(idx + num, flag_num, num):
                    prime_flag[j] = False

        primes = [2]
        temp = [(i + 1) * 2 + 1 for i in range(flag_num) if prime_flag[i]]
        primes.extend(temp)

        return primes

    primes = enum_primes(10 ** 6)

    for prime in primes:
        if prime >= X:
            return print(prime)


if __name__ == '__main__':
    main()
