def answer(k: int, s: str) -> str:
    return s if len(s) <= k else s[:k] + '...'


def main():
    k = int(input())
    s = input()
    print(answer(k, s))


if __name__ == '__main__':
    main()