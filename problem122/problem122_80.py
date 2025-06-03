def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline
    input()
    a = tuple(map(int, input().split()))
    ans = sum(a)
    a = Counter(a)
    for _ in range(int(input())):
        b, c = map(int, input().split())
        if b in a:
            ans += (c - b) * a[b]
            a[c] = a[c] + a[b] if c in a else a[b]
            del a[b]
        print(ans)


if __name__ == "__main__":
    main()