while True:
    W = input().rstrip()
    if W == "-":
        break
    m = int(input().rstrip())
    l = list(W)
    for i in range(m):
        h = int(input().rstrip())
        w = l[:h]
        del l[:h]
        l += w
    ans = "".join([str(i) for i in l])
    print(ans)
