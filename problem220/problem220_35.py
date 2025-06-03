import sys
input = sys.stdin.readline


def main():
    S, T = input().split()
    A, B = map(int, input().split())
    U = input().strip()
    print(A-1, B) if S == U else print(A, B-1)


if __name__ == '__main__':
    main()
