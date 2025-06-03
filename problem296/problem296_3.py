def main3():
    s = input()
    k = int(input())

    if len(set(s)) == 1:
        print(len(s)*k//2)
    else:
        s1 = list(s)
        s2 = list(s + s)

        c1, c2 = 0, 0
        for i in range(len(s1) - 1):
            if s1[i] == s1[i + 1]:
                    c1 += 1
                    s1[i + 1] = "-"

        for i in range(len(s2) - 1):
            if s2[i] == s2[i + 1]:
                    c2 += 1
                    s2[i + 1] = "-"

        d = c2 - c1
        print(c1 + (k - 1) * d)

if __name__ == "__main__":
    main3()