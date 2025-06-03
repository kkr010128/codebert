while True:
    l=list(input())
    if l==["0"]:
        break
    print(sum(map(int,l)))