d = input().split()
cmd_list = list(input())
w = []

for cmd in cmd_list:
    if cmd == "E":
        w = d
        d[0], d[1], d[2], d[3], d[4], d[5] = w[3], w[1], w[0], w[5], w[4], w[2]
    elif cmd == "N":
        w = d
        d[0], d[1], d[2], d[3], d[4], d[5] = w[1], w[5], w[2], w[3], w[0], w[4]
    elif cmd == "S":
        w = d
        d[0], d[1], d[2], d[3], d[4], d[5] = w[4], w[0], w[2], w[3], w[5], w[1]
    elif cmd == "W":
        w = d
        d[0], d[1], d[2], d[3], d[4], d[5] = w[2], w[1], w[5], w[0], w[4], w[3]

print(d[0])

