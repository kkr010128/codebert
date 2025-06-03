def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors


def main():
    n = int(input())
    # 1回も割り算しない場合は n mod k = 1でkは(n-1)の約数
    ans = len(make_divisors(n - 1)) - 1
    # 割り算をする場合
    l = make_divisors(n)[1:]
    for i in l:
        num = n
        while num % i == 0:
            num //= i
        if num % i == 1:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
