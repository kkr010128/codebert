from sys import stdin


def main():
    s = stdin.readline()[:-1]
    print('Yes') if s[2] == s[3] and s[4] == s[5] else print('No')


if __name__ == "__main__":
    main()
