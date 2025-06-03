x = int(input())

rl = 400

for i in range(8, 0, -1):
    if (rl <= x) and (x <= rl+199):
        print(i)
    rl += 200