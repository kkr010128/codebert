from numba import njit


@njit(fastmath=True)
def fact(x):
    i = 1
    while i * i <= x:
        if x % i == 0:
            yield i
            yield x // i
        i += 1


def main():
    n = int(input())
    a = tuple(map(int, input().split()))

    c = [0] * (max(a) + 1)

    for e in a:
        c[e] += 1

    ans = n
    for e in a:
        c[e] -= 1
        for fct in fact(e):
            if c[fct]:
                ans -= 1
                break

        c[e] += 1

    print(ans)


if __name__ == "__main__":
    main()
