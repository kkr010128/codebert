if __name__ == '__main__':
    from sys import stdin
    from itertools import combinations

    while True:
        n, x = (int(n) for n in stdin.readline().rstrip().split())

        if n == x == 0:
            break

        a = range(1, n + 1)
        l = tuple(filter(lambda _: sum(_) == x, combinations(a, 3)))

        print(len(l))
