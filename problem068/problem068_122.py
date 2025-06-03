str = input()
lstr = list(str)

num = int(input())

for i in range(num):
    order = input().split()

    if (order[0] == "print"):
        onum = list(map(int,order[1:3]))

        for i in range(onum[0],onum[1]+1):
            print(lstr[i],end = "")
        print("")

    elif (order[0] == "reverse"):
        onum = list(map(int,order[1:3]))
        if (onum[0] == 0):
            tmp1 = lstr[0:onum[1]+1]
            tmp1.reverse()
            tmp2 = lstr[onum[1]+1:]
            lstr = tmp1 + tmp2

        else:
            tmp1 = lstr[:onum[0]]
            tmp2 = lstr[onum[0]:onum[1]+1]
            tmp2.reverse()
            tmp3 = lstr[onum[1]+1:]
            lstr = tmp1 + tmp2 +tmp3

    elif (order[0] == "replace"):
        onum = list(map(int,order[1:3]))
        restr = list(order[3])

        for i in range(onum[0],onum[1]+1):
            lstr[i] = restr[i-onum[0]]

