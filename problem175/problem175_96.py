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
    for j in range(1, n):
        for i in range(j):
            k = 2 * j - i
            if k >= n:
                continue
            if s[i] == s[j] or s[j] == s[k] or s[k] == s[i]:
                continue
            cnt += 1

    print(len(r_set) * len(g_set) * len(b_set) - cnt)


if __name__ == "__main__":
    main()
