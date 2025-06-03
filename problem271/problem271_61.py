a = int(input())
b = input()
for i in range(0, len(b)):
    c = ord(b[i])
    d = int(c+a)
    if d>90:
        d -= 26
    e = chr(d)
    print(e, end="")