def main():
    while True:
        n, x = map(int, input().split())
        if n == x == 0:
            break
        number = 0
        for i in range(n):
            j = i + 1
            if x - j > n*2 - 1:
                continue
            elif x - j <= j:
                break
            else:
                for k in range(x - j):
                    m = k + 1
                    if k < j:
                        continue
                    elif (x - j - m) > m and x - j - m <= n:
                        number += 1

        print(number)
    return


if __name__ == '__main__':
    main()

