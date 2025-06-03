def main():
    n = int(input())
    s = input()
    r_set, g_set, b_set = set(), set(), set()

    for i, c in enumerate(s):
        if c == "R":
            r_set.add(i)
        elif c == "G":
            g_set.add(i)
        elif c == "B":
            b_set.add(i)

    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            k = 2 * j - i

            if i in r_set and j in g_set and k in b_set:
                cnt += 1
            elif i in r_set and j in b_set and k in g_set:
                cnt += 1
            elif i in g_set and j in r_set and k in b_set:
                cnt += 1
            elif i in g_set and j in b_set and k in r_set:
                cnt += 1
            elif i in b_set and j in r_set and k in g_set:
                cnt += 1
            elif i in b_set and j in g_set and k in r_set:
                cnt += 1

    print(len(r_set) * len(g_set) * len(b_set) - cnt)


if __name__ == "__main__":
    main()
