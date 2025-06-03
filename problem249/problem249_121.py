def main():
    a, b, k = map(int, input().split())

    if a >= k:
        remain_a = a - k
        remain_b = b
    else:
        remain_a = 0
        if k - a >= b:
            remain_b = 0
        else:
            remain_b = b - (k - a)

    print(remain_a, remain_b)


if __name__ == "__main__":
    main()
