import sys


def resolve(in_):
    N, K = map(int, next(in_).split())
    A = map(int, next(in_).split())
    number_plus1 = list(i + 1 for i in A)

    v = [0] * N
    v[0] = sum(number_plus1[:K])
    for i, (before, after) in enumerate(zip(number_plus1, number_plus1[K:]), 1):
        v[i] = v[i - 1] - before + after

    expected = max(v) / 2

    return expected


def main():
    answer = resolve(sys.stdin.buffer)
    print(f'{answer:.12f}')


if __name__ == '__main__':
    main()
