def main():
    d, t, s = map(int, input().split())

    print('Yes' if t*s >= d else 'No')


if __name__ == '__main__':
    main()
