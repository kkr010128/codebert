s = list(input())
n = int(input())
for i in range(n):
    d = input().split(" ")
    if d[0] == "replace":
        a = int(d[1])
        b = int(d[2])
        c = list(d[3])
        k = 0
        for j in range(a, b+1):
            s[j] = c[k]
            k += 1
    elif d[0] == "reverse":
        a = int(d[1])
        b = int(d[2])
        c = list(s)
        k = b
        for j in range(a, b+1):
            s[j] = c[k]
            k -= 1
    else:
        a = int(d[1])
        b = int(d[2])
        for j in range(a, b+1):
            print(s[j],end="")
        print("")