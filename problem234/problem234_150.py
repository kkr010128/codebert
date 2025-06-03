import sys


def input():
    return sys.stdin.readline().strip()


def main():
    N = int(input())
    C = [[0] * 10 for _ in range(10)]
    for i in range(10):
        for j in range(10):
            for n in range(1, N + 1):
                L = len(str(n)) - 1
                a = n // (10 ** L)
                b = n % 10
                if a == i and b == j:
                    C[i][j] += 1
    answer = 0
    for i in range(10):
        for j in range(10):
            answer += C[i][j] * C[j][i]
    print(answer)


if __name__ == "__main__":
    main()
