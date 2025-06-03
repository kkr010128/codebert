def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    plus = []
    minus = []
    total = 0
    for _ in range(N):
        s = input().strip()
        h = 0
        bottom = 0
        for ss in s:
            if ss == "(":
                h += 1
            else:
                h -= 1
                bottom = min(bottom, h)
        total += h
        if h > 0:
            plus.append((bottom, h))
        else:
            minus.append((bottom-h, -h))
    if total != 0:
        print("No")
        sys.exit()
    plus.sort(reverse=True)
    minus.sort(reverse=True)
    height = 0
    for b, h in plus:
        if height + b < 0:
            print("No")
            sys.exit()
        height += h
    height = 0
    for b, h in minus:
        if height + b < 0:
            print("No")
            sys.exit()
        height += h
    print("Yes")
        


if __name__ == '__main__':
    main()