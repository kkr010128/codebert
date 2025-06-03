def main():
    n = int(input())
    div, mod = divmod(n, 2)
    if mod != 0:
        print(div + 1)
    else:
        print(div)


if __name__ == '__main__':
    main()