import sys


def resolve(in_):
    s, w = map(int, next(in_).split())
    return 'safe' if s > w else 'unsafe'


def main():
    answer = resolve(sys.stdin.buffer)
    print(answer)


if __name__ == '__main__':
    main()