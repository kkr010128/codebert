def f(h):
    if h == 1:
        return 1
    return 2 * f(h // 2) + 1


def main():
    h = int(input())

    ans = f(h)

    print(ans)


if __name__ == "__main__":
    main()
