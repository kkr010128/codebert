import sys


def log(s):
    # print("| " + str(s), file=sys.stderr)
    pass


def output(x):
    print(x, flush=True)


def input_ints():
    return list(map(int, input().split()))


def main():
    f = input_ints()
    print(f[0] * f[1])


main()
