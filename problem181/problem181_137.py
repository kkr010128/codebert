import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    K = int(readline())

    vec = list(range(1, 10))
    for i in range(K):
        tail = vec[i] % 10
        n10 = vec[i] * 10
        if tail == 0:
            vec.append(n10 + tail)
            vec.append(n10 + tail + 1)
        elif tail == 9:
            vec.append(n10 + tail - 1)
            vec.append(n10 + tail)
        else:
            vec.append(n10 + tail - 1)
            vec.append(n10 + tail)
            vec.append(n10 + tail + 1)

    print(vec[K - 1])
    return


if __name__ == '__main__':
    main()
