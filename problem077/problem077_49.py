def main():
    a, b, c, d = (int(i) for i in input().split())
    print(max(a*c, b*d, a*d, b*c))


if __name__ == '__main__':
    main()
