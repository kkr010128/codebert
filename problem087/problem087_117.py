def main():
    n = input()
    res = 0
    for ni in n:
        res = (res + int(ni)) % 9

    print(('Yes', 'No')[res != 0])


if __name__ == '__main__':
    main()
