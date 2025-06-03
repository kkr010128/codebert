i = int(input())
h = i // 3600
i -= h * 3600
m = i // 60
i -= m * 60
s = i
print("{}:{}:{}".format(h, m, s))

