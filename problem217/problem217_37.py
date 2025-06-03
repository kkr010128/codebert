def main():
    n = int(input())
    A = list(map(int, input().split()))

    for a in A:
        if a % 2 == 0:
            if not (a % 3 == 0 or a % 5 == 0):
                print('DENIED')
                return
    print('APPROVED')


if __name__ == '__main__':
    main()
