import sys


def resolve(in_):
    N = int(next(sys.stdin.buffer))
    P = map(int, next(sys.stdin.buffer).split())

    min_ = 200001
    ans = 0
    for p in P:
        if p <= min_:
            ans += 1
            min_ = p
    return ans


def main():
    answer = resolve(sys.stdin.buffer)
    print(answer)


if __name__ == '__main__':
    main()
