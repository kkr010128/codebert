def main():
    from collections import Counter
    s = input()

    l = [0]
    t = 1
    for i, x in enumerate(s[::-1]):
        t = t * 10 % 2019
        y = (l[-1] + int(x) * t) % 2019
        l.append(y)

    c = Counter(l)
    ans = sum([v * (v - 1) // 2 for v in c.values()])
    print(ans)


if __name__ == '__main__':
    main()
