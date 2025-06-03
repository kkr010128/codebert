from sys import stdin


def main():
    x, y, a, b, c = map(int, stdin.readline().split())
    p = list(map(int, stdin.readline().split()))
    q = list(map(int, stdin.readline().split()))
    r = list(map(int, stdin.readline().split()))

    pqr = []

    for pi in p:
        pqr.append([pi, 0])
    for qi in q:
        pqr.append([qi, 1])
    for ri in r:
        pqr.append([ri, 2])

    pqr.sort(reverse=True)

    ans = 0
    c_a = 0
    c_b = 0
    c_c = 0

    for pqri in pqr:
        if pqri[1] == 0 and c_a < x:
            ans += pqri[0]
            c_a += 1
        elif pqri[1] == 1 and c_b < y:
            ans += pqri[0]
            c_b += 1
        elif pqri[1] == 2 and (c_a < x or c_b < y) and c_a + c_b + c_c < x + y:
            ans += pqri[0]
            c_c += 1
        if c_a + c_b + c_c == x + y:
            print(ans)
            exit()


if __name__ == "__main__":
    main()
