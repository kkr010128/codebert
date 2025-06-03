from math import sqrt


def is_prime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False

    return True


def make_divisors(a, b):
    lower_divisors = []
    upper_divisors = []

    i = 1
    n = min(a, b)
    m = max(a, b)

    while i*i <= n:
        if n % i == 0:
            # 大きい方の数が割れるか確認
            if m % i == 0:
                # 素数であるか確認
                if is_prime(i):
                    lower_divisors.append(i)

            # 割り切れる場合 i で割った数も約数
            if i != n // i:

                # i で割った数で大きいほうが割り切れるか
                if m % (n // i) == 0:

                    # 素数であるか
                    if is_prime(n//i):
                        upper_divisors.append(n//i)
        i += 1

    return lower_divisors + upper_divisors[::-1]


def main():
    A, B = [int(x) for x in input().split()]
    divisors = make_divisors(A, B)
    print(len(divisors))


if __name__ == '__main__':
    main()
