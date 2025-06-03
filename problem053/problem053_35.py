def az15():
    n = input()
    xs = map(int,raw_input().split())
    xs.reverse()
    for i in range(0,len(xs)):
        print xs[i],
az15()