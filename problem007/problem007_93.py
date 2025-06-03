import sys

input = sys.stdin.readline


def main():
    n = int(input())

    fib = [1] * 46
    for i in range(2, 46):
        fib[i] = fib[i - 1] + fib[i - 2]

    ans = fib[n]
    print(ans)


if __name__ == "__main__":
    main()

