for _ in range(int(input())):
    e = list(map(int, input().split()))
    print("YES" if max(e) ** 2 * 2 == sum(i ** 2 for i in e) else "NO")
