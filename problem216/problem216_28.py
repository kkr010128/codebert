import sys


def main():
    input = sys.stdin.buffer.readline
    a, b, c = map(int, input().split())
    if len(set([a, b, c])) == 2:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
