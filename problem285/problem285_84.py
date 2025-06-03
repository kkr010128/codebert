def main():
    S = input()
    N = len(S)

    ret = [0] * (N + 1)

    for i, c in enumerate(S, start=1):
        if c == '<':
            ret[i] = max(
                ret[i],
                ret[i - 1] + 1
            )

    for i, c in enumerate(reversed(S), start=1):
        i = N - i
        if c == '>':
            ret[i] = max(
                ret[i],
                ret[i + 1] + 1
            )

    print(sum(ret))


if __name__ == '__main__':
    main()
