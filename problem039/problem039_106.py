def funcs(a, b, c):
    x = int(a)
    y = int(b)
    z = int(c)

    if x < y < z:
        print("Yes")
    else:
        print("No")


tmp = input()

a, b, c = tmp.split(" ")

funcs(a, b, c)

