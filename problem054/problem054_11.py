def search(num, items, Mark):
    printlist = []
    for i in range(num):
        if not(i+1 in items):
            print(Mark, i+1)

n = int(input())
Slist = []
Hlist = []
Clist = []
Dlist = []
for i in range(n):
    MN = input().split()
    mark = MN[0]
    number = int(MN[1])
    if mark == "S":
        Slist.append(number)
    elif mark == "H":
        Hlist.append(number)
    elif mark == "C":
        Clist.append(number)
    else:
        Dlist.append(number)
    i = i+1

search(13, Slist, "S")
search(13, Hlist, "H")
search(13, Clist, "C")
search(13, Dlist, "D")