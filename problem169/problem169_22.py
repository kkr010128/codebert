import sys


def resolve(in_, out):
    n = int(in_.readline())
    b = [0] * (n + 1)
    for a in map(int, in_.readline().split()):
        b[a] += 1
    out.write('\n'.join(map(str, b[1:])))


def main():
    resolve(sys.stdin.buffer, sys.stdout)


if __name__ == '__main__':
    main()