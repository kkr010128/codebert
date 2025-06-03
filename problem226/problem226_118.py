def main():
    H, _ = map(int, input().split())
    A = map(int, input().split())

    cond = sum(A) >= H

    print('Yes' if cond else 'No')


if __name__ == '__main__':
    main()
