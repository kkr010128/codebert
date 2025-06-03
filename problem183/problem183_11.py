def main():
    N = int(input())

    def enum_divisors(n):
        # 約数列挙
        divs = []
        for i in range(1, n+1):
            if i*i > n:
                break
            if n % i == 0:
                divs.append(i)
                if n//i != i:
                    # i が平方数でない
                    divs.append(n//i)
        return divs

    ans = 0
    for k in enum_divisors(N-1):
        if 2 <= k:
            ans += 1

    for k in enum_divisors(N):
        if 2 <= k:
            n = N
            while n > 1 and n % k == 0:
                n //= k
            if n % k == 1:
                ans += 1

    print(ans)


if __name__ == '__main__':
    main()
