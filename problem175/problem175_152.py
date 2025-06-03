def main():
    n = int(input())
    s = input()
    if n < 4:
        print(0)
        return
    ans = s.count("R") * s.count("G") * s.count("B")

    for i, si in enumerate(s[:-2]):
        for j, sj in enumerate(s[i+1:-1]):
            if si == sj:
                continue

            if i + 2*j+2 < n and si != s[i + 2*j+2] != sj:
                ans -= 1

    print(ans)


if __name__ == '__main__':
    main()
