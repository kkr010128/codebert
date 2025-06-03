import sys
input = sys.stdin.readline


def main():
    N = int(input())
    print(N//2+1) if N % 2 else print(N//2)


if __name__ == '__main__':
    main()
