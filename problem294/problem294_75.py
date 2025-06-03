import bisect


def main():
    n = int(input())
    l = sorted(list(int(i) for i in input().split()))

    cnt = 0

    for i in range(n - 2):
        a = l[i]
        for j in range(i + 1, n-1):
            b = l[j]
            cnt += bisect.bisect_left(l, a+b)-(j+1)

    print(cnt)


if __name__ == "__main__":
    main()
