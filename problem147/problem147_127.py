def main():
    S = input()
    T = input()

    cond = 1 <= len(S) <= 10
    cond = cond and (len(T) == len(S) + 1)
    cond = cond and (T[:-1] == S)

    print('Yes' if cond else 'No')


if __name__ == '__main__':
    main()
