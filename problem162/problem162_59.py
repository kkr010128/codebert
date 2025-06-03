def main():
    N, M = map(int, input().split())  # N must be an odd number

    left = 1
    count = 0
    buff = 0
    for d in range(N-1, 0, -2):

        if (N-1) & 1 and d <= -d % N:
            buff = 1

        right = left + d - buff
        print(left, right)

        left += 1
        count += 1
        if count == M:
            return


if __name__ == "__main__":
    main()
