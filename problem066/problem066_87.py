m = ""
while True:
    S = input()
    if S == "-":
        break

    S = list(S)
    L = S
    n = int(input())
    for i in range(n):
        m = int(input())
        for j in range(m):
            t = L.pop(0)
            L.append(t)

    L = "".join(L)
    print(L)