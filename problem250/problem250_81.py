def main():
    X = int(input())
    if X == 2:
        print(2)
        exit()
    if X % 2 == 0:
        X += 1
    while True:
        flag = True
        for i in range(3, X, 2):
            if X % i == 0:
                flag = False
                break
        if flag is True:
            print(X)
            break
        else:
            X += 2


if __name__ == '__main__':
    main()
