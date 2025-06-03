while True:
    n = raw_input()
    if n == "-":
        break
    m = int(raw_input())
    for i in range(0,m):
        h = int(raw_input())
        under = n[0:h]
        n = n[h:]+under
    print n