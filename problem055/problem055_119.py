build = [[[0]*10,[0]*10,[0]*10],[[0]*10,[0]*10,[0]*10],[[0]*10,[0]*10,[0]*10],[[0]*10,[0]*10,[0]*10]]
n = int(input())
for i in range(n):
    b, f, r, v = [int(x) for x in input().split()]
    build[b-1][f-1][r-1] += v
count = 0
for i1 in build:
    for i2 in i1:
        line = ""
        for i3 in i2:
            line += " " + str(i3)
        print(line)
    if count < 3:
        print("#"*20)
        count += 1