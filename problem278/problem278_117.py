from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    print(int(input()) ** 2)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
