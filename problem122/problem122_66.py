def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline
    input()
    a = list(map(int, input().split()))
    ans = sum(a)
    a = Counter(a)
    for _ in range(int(input())):
        b, c = map(int, input().split())
        if b in a:
            ans += (c - b) * a[b]
            print(ans)
            if c in a:
                a[c] += a[b]
            else:
                a[c] = a[b]
            del a[b]
        else:
            print(ans)


if __name__ == "__main__":
    main()