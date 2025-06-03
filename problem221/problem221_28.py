def main():
    s = list(input())

    for i in range(len(s)):
        s[i] = "x"

    L = "".join(s)
    print(L)


if __name__ == "__main__":
    main()
