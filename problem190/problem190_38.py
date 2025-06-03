def main():
    S = input()
    L = len(S)

    def check(s):
        return s == s[::-1]

    cond = check(S)
    cond = cond and check(S[:L // 2])
    cond = cond and check(S[(L + 1) // 2:])

    print('Yes' if cond else 'No')


if __name__ == '__main__':
    main()
