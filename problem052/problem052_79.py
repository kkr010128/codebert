def call(n):
    s = ""
    for x in range(1, n + 1):
        y = x
        if y % 3 == 0:
            s = s + " " + str(x)
        else:
            while y != 0:
                if y % 10 == 3:
                    s = s + " " + str(x)
                    break
                y = int(y / 10)
    return s

n = int(input())
print(call(n))