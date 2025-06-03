from sys import stdin, setrecursionlimit


def main():
    s, t = map(str, stdin.readline().split())
    a, b = map(int, stdin.readline().split())
    u = stdin.readline()[:-1]

    if s == u:
        a -= 1
    else:
        b -= 1

    print(a, b)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()