def main():
    n = int(input())
    ans = 0
    m = n - 1
    num = 1
    while num * num <= m:
        if m % num == 0:
            if num > 1:
                ans += 1
            if m // num != num:
                ans += 1
        num += 1
    num = 1
    while num * num <= n:
        if n % num == 0:
            tmp = n
            while num > 1 and tmp % num == 0:
                tmp = tmp // num
            if tmp == 1 or tmp % num == 1:
                ans += 1
            rest = n // num
            if rest != num:
                tmp = n
                while tmp % rest == 0:
                    tmp = tmp // rest
                if tmp == 1 or tmp % num == 1:
                    ans += 1
        num += 1
    print(ans)


if __name__ == "__main__":
    main()
