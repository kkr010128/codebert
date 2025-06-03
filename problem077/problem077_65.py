def main():
    a, b, c, d = map(int, input().split())
    ans = max([a * c, b * d, a * d, b * c])
    print(ans)


if __name__ == "__main__":
    main()
