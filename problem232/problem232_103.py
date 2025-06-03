def answer(a: int, b: int) -> str:
    return min(str(a) * b, str(b) * a)


def main():
    a, b = map(int, input().split())
    print(answer(a, b))


if __name__ == '__main__':
    main()