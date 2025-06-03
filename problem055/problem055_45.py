l = [[[0 for r in range(10)] for f in range(3)] for b in range(4)]
n = int(input())
for num in range(n):
    b,f,r,v = [int(x) for x in input().split()]
    l[b-1][f-1][r-1] += v
for b in range(4):
    for f in range(3):
        for r in range(10):
            print('', l[b][f][r], end='')
        print("")
    if b != 3:
        print("#" * 20)