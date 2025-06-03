while True:
    n = int(input())
    if n == 0:
        break
    else:
        score = [int(x) for x in input().split()]
        a = 0
        m = sum(score)/n
    for s in score:
        a += (s-m)**2
    a = (a/n)**0.5
    print('{:.8f}'.format(a))

