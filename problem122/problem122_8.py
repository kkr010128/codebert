def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline
    input()
    a = Counter(map(int, input().split()))
    ans = sum(k * v for k, v in a.items())
    for _ in range(int(input())):
        b, c = map(int, input().split())
        if b in a:
            ans += (c - b) * a[b]
            print(ans)
            a[c] = a[c] + a[b] if c in a else a[b]
            del a[b]
        else:
            print(ans)


if __name__ == "__main__":
    main()