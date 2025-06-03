def main():
    num = int(input())
    con = 10**9 + 7
    a, b, c = 1, 1, 2
    for i in range(num):
        a *= 10
        a %= con
        b *= 8
        b %= con
        c *= 9
        c %= con
    if(a+b-c < 0):
        print(a+b-c+con)
        return 0
    print(a+b-c)


if __name__ == '__main__':
    main()
