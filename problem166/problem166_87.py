import sys

input = sys.stdin.readline
P = 2019


def main():
    S = input().rstrip()

    N = len(S)
    count = [0] * P
    count[0] += 1
    T = 0
    for i in range(N):
        T = (T + int(S[(N - 1) - i]) * pow(10, i, mod=P)) % P
        count[T] += 1

    ans = 0
    for k in count:
        ans = (ans + k * (k - 1) // 2)
    print(ans)


if __name__ == "__main__":
    main()
