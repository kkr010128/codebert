def main():
    input()
    array = [int(x) for x in input().split()]
    ans = sum(x % 2 == 1 for x in array[::2])
    print(ans)


if __name__ == '__main__':
    main()
