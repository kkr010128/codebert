from math import floor


def main():
    A, B, N = map(int, input().split())
    if N >= B-1:
        x = B - 1
    else:
        x = N

    print(floor((A*x)/B) - A*floor(x/B))


if __name__ == '__main__':
    main()
