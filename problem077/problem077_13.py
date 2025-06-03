from sys import stdin


def main():
    _in = [_.rstrip() for _ in stdin.readlines()]
    a, b, c, d = list(map(int, _in[0].split(' ')))  # type:list(int)
    # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    ans = -float('inf')
    for _ in [a * c, a * d, b * c, b * d]:
        ans = max(ans, _)
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    print(ans)


if __name__ == "__main__":
    main()
