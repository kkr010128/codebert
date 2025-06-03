while True:
    n = int(input())
    if n == 0:
        break
    scores = [int(x) for x in input().split()]
    ave = sum(scores)/n
    resi = 0
    for s in scores:
        resi += (s-ave)**2
    sd = (resi/n)**0.5
    print('{:.6f}'.format(sd))

