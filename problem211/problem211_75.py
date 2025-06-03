import sys
input = sys.stdin.readline


def main():
    N, R = map(int, input().split())
    print(R+100*(10-N)) if N < 10 else print(R)


if __name__ == '__main__':
    main()
