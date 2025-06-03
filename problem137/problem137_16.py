import statistics


def main():
    n = int(input())
    a = [0 for _ in range(n)]
    b = [0 for _ in range(n)]
    for i in range(n):
        a[i], b[i] = map(int, input().split())

    amed = statistics.median(a)
    bmed = statistics.median(b)

    if n % 2:
        print(int(bmed - amed + 1))
    else:
        print(int((bmed - amed) * 2 + 1))


if __name__ == '__main__':
    main()
