while True:
    i = list(map(int,list(input())))
    if i == [0]:
        break
    else:
        print(sum(i))