import sys


if __name__ == "__main__":
    n, m = map(lambda x: int(x), input().split())
    coins = list(map(lambda x: int(x), input().split()))

    table = [sys.maxsize] * (n + 2)
    table[0] = 0
    for i in range(n + 1):
        for coin in coins:
            if (i + coin <= n):
                table[i + coin] = min(table[i + coin], table[i] + 1)

    print(table[n])

