while True:
    c = str(input())
    if c == "-":
        break
    n = int(input())
    for i in range(n):
        a = int(input())
        c = c[a:] + c[:a]
    print(c)

