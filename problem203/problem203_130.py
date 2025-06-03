import sys


def resolve(in_):
    A, B = map(int, in_.readline().split())

    for i in range(1, 1251):
        if i * 8 // 100 == A and i // 10 == B:
            return i 

    return -1


def main():
    answer = resolve(sys.stdin.buffer)
    print(answer)


if __name__ == '__main__':
    main()
