# coding: utf-8


def main():
    X = int(input())
    C = X // 100
    print([0, 1][X >= C * 100 and X <= C * 105])


if __name__ == "__main__":
    main()
