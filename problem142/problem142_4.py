def main():
    n = input()
    m = int(n[-1])
    hon = [2, 4, 5, 7, 9]
    pon = [0, 1, 6, 8]
    if m in hon:
        print('hon')
    elif m in pon:
        print('pon')
    else:
        print('bon')


if __name__ == '__main__':
    main()