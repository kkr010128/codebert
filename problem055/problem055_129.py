n = int(input())
Building = [[[0 for r in range(11)] for f in range(4)] for b in range(5)]
for i in range(n):
    b, f, r, v = map(int, input().split())
    Building[b][f][r] += v

for b in range(1, 5):
    for f in range(1, 4):
        for r in range(1, 11):
            print(" " + str(Building[b][f][r]), end = "")
        print()
    if b != 4:
        print("####################")