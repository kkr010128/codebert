def main():
    N = int(input())
    S = input()

    cond = S[:N // 2] == S[N // 2:]

    print('Yes' if cond else 'No')


if __name__ == '__main__':
    main()
