def main():
    n = int(input())
    plus = []
    minus = []

    for _ in range(n):
        x, y = map(int, input().split())
        plus.append(x + y)
        minus.append(x - y)

    plus_max = max(plus)
    plus_min = min(plus)
    minus_max = max(minus)
    minus_min = min(minus)

    print(max(plus_max - plus_min, minus_max - minus_min))


if __name__ == "__main__":
    main()