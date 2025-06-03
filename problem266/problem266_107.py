def main():
    X = int(input())
    if X < 100:
        print(0)
    elif 2000 <= X:
        print(1)
    else:
        a = X // 100
        b = a * 5
        if X % 100 <= b:
            print(1)
        else:
            print(0)


if __name__ == '__main__':
    main()
