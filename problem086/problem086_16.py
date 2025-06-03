import sys


def resolve(in_):
    N, X, T = map(int, next(in_).split())

    minute = 0
    tako = 0
    while tako < N:
        tako += X
        minute += T

    return minute

def main():
    answer = resolve(sys.stdin)
    print(answer)


if __name__ == '__main__':
    main()
