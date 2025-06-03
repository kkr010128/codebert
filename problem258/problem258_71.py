def main():
    n = int(input())
    if n < 10 or n % 2 == 1:
        print(0)
    else:
        ans = 0
        i = 10
        while i <= n:
            ans += n // i
            i *= 5
        print(ans)

if __name__ == '__main__':
    main()
