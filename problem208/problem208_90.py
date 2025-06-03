import sys
import itertools

def resolve(in_):
    N, M = map(int, in_.readline().split())
    sc = tuple(tuple(map(int, line.split())) for line in itertools.islice(in_, M))

    if N == 1:
        values = range(10)
    else:
        values = range(10 ** (N - 1), 10 ** N)

    for value in values:
        if all(value // (10 ** (N - s)) % 10 == c for s, c in sc):
            return value

    return -1


def main():
    answer = resolve(sys.stdin.buffer)
    print(answer)


if __name__ == '__main__':
    main()
