while True:
    N=input()
    if N=="0":
        break
    else:
        print(sum([int(x) for x in list(N)]))