def main():
    n = int(input())
    if n % 2 == 0 and n >= 10:
        m = n // 2
        k = 5
        m5 = 0
        while k <= m:
            m5 += m // k
            k *= 5
    else:
        m5 = 0

    print(m5)


if __name__ == '__main__':
    main()
