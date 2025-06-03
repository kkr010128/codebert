a, b, c, d = map(int, input().split(" "))
print(max([i for i in [i*j for i in (a, b) for j in (c,d)]]))