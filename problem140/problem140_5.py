def resolve():
    t = input()
    s = ""
    for c in t:
        if c == "?":
            c = "D"

        s += c
    print(s)

resolve()