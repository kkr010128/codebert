def main():
    N = input()
    acc = 0
    for idx in range(len(N)):
        acc += (ord(N[idx]) - ord('0'))

    print('Yes') if not acc % 9 else print('No')


if __name__ == '__main__':
    main()
