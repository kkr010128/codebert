import sys


def resolve(in_):
    L = int(in_.read())
    return (L / 3.0) ** 3


def main():
    answer = resolve(sys.stdin)
    print(f'{answer:.12f}')


if __name__ == '__main__':
    main()
