def main():
    from itertools import permutations
    from math import hypot

    N = int(input())

    xys = []
    for _ in range(N):
        x, y = map(int, input().split())
        xys.append((x, y))

    ans = 0
    for perm in permutations(xys, r=2):
        x1, y1 = perm[0]
        x2, y2 = perm[1]
        d = hypot(x2 - x1, y2 - y1)
        ans += d
    ans /= N

    print(ans)


if __name__ == '__main__':
    main()
