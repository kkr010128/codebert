def main():
    num, target = map(int, input().split())
    if num * 500 >= target:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()