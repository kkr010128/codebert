while True:
    s = input()
    if s == '-':
        break
    m = int(input())
    for _ in range(m):
        h = int(input())
        ns = s[h:] + s[:h]
        s = ns
    print(s)

