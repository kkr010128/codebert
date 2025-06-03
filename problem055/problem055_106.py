from sys import stdin

rooms = [[[0] * 10 for _ in range(3)] for _ in range(4)]
stdin.readline().rstrip()
while True:
    try:
        b, f, r, v = [int(x) for x in stdin.readline().rstrip().split()]
        rooms[b-1][f-1][r-1] += v
    except:
        break

for b in range(4):
    for f in range(3):
        print(" ", end = "")
        print(*rooms[b][f])
    else:
        if b != 3:
            print("#"*20)
