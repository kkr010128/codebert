def main():
    x, n = map(int, input().split())
    ps = list(map(int, input().split()))

    for i in range(n//2 + 2):
        if x - i not in ps:
            print(x-i)
            return
        if x + i not in ps:
            print(x+i)
            return


if __name__ == '__main__':
    main()
