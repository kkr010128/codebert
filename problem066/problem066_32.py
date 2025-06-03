while True:
    n = str(input())
    if n == "-":
        break
    m = int(input())
    for i in range(m):
        h=int(input())
        n = n[h:len(n)] + n[0:h]
    print(n)
