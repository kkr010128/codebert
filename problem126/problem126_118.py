lx = [int(w) for w in input().split()]

for i, x in enumerate(lx):
    if x == 0:
        print(i+1)
        exit()
