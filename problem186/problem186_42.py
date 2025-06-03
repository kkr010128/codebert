import sys


def main():
    read = sys.stdin.buffer.read
    k, n, *A = map(int, read().split())
    far = k + A[0] - A[-1]
    y = A[0]
    for x in A[1:]:
        dis = x - y
        if far < dis:
            far = dis
        y = x
    print(k - far)


if __name__ == "__main__":
    main()