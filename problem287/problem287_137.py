def main():
    N = int(input())

    def check():
        for i in range(1, 10):
            for j in range(1, 10):
                if i * j == N:
                    return True
        return False

    cond = check()

    print('Yes' if cond else 'No')


if __name__ == '__main__':
    main()
