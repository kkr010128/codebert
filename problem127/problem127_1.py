def main():
    x, y = map(int, input().split())

    print('Yes' if 2*x <= y <= 4*x and y % 2 == 0 else 'No')


if __name__ == '__main__':
    main()
