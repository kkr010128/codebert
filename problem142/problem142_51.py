def main():
    n = input()
    hon = ['2', '4', '5', '7', '9']
    pon = ['0', '1', '6', '8']
    bon = ['3']
    if n[len(n)-1] in hon:
        print('hon')
    elif n[len(n)-1] in pon:
        print('pon')
    else:
        print('bon')


if __name__ == "__main__":
    main()
