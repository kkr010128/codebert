def main():
    n = int(input())
    ans = n

    for i in range(1, int(n ** 0.5) + 1):
        if n % i != 0:
            continue
        j = n // i
        ans = min(ans, i + j - 2)

    print(ans)


if __name__ == "__main__":
    main()
