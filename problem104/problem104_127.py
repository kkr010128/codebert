def main():
    left, right, div = [int(x) for x in input().split()]
    ans = right // div - (left - 1) // div
    print(ans)


if __name__ == '__main__':
    main()
