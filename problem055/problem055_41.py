def az17():
    a = [[[0 for r in range(10)] for f in range(3)] for b in range(4)]
    n = input()
    for i in range(n):
        xs = map(int,raw_input().split())
        a[xs[0]-1][xs[1]-1][xs[2]-1] = a[xs[0]-1][xs[1]-1][xs[2]-1] + xs[3]
    for b in range(0,4):
        for f in range(0,3):
            print "",
            for r in range(0,10):
                print a[b][f][r],
            print
        if not b == 3:
            print "#"*20

az17()