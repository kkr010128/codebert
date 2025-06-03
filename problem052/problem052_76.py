def func(n):
    i = 1
    dst = ""

    def include3(x, i):
        local_dst = ""

        if x % 10 == 3:
            local_dst += " " + str(i)
        else:
            if x // 10:
                local_dst += include3(x // 10, i)

        return local_dst

    while i <= n:
        x = i
        if x % 3 == 0:
            dst += " " + str(i)
        else:
            dst += include3(x, i)
        i += 1

    return dst

print(func(int(input())))