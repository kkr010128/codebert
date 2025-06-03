def call(n):
    ans = []

    for i, x in enumerate(range(1, n + 1), 1):
        if x % 3 == 0:
            ans.append(i)
            continue

        while x:
            if x % 10 == 3:
                ans.append(i)
                break
            x //= 10

    print(" " + " ".join(map(str, ans)))


if __name__ == '__main__':
    from sys import stdin

    n = int(stdin.readline().rstrip())

    call(n)

