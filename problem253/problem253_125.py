def main():
    n, a, b = map(int, input().split())

    if (b - a) % 2 == 0:
        ans = (b - a) // 2
    else:
        if b - 1 < n - a:
            g = (b - a + 1) // 2
            ans = a + g - 1
        else:
            g = (2 * n + a - b + 1) // 2
            ans = 2 * n - b - g + 1
    
    print(ans)


if __name__ == "__main__":
    main()
