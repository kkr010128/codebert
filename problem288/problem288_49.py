def main():
    n = int(input())
    ans = 10000000000000
    for i in range(1, int(n ** 0.5 + 0.5) + 1):
        if n % i == 0:
            ans = min(ans, i + n // i - 2)
    print(ans)


if __name__ == '__main__':
    main()
