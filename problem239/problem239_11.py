import sys
from string import ascii_lowercase as a2z

input = sys.stdin.readline


def main():
    C = input().rstrip()

    i = a2z.index(C)
    ans = a2z[i + 1]
    print(ans)


if __name__ == "__main__":
    main()
