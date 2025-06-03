def main():
    a, b = input().split()
    if a < b:
        ans = a * int(b)
    else:
        ans = b * int(a)
    print(ans)


if __name__ == '__main__':
    main()
