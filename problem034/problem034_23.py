def right_num(m,u):
    cube = [
        {2:3,3:5,4:2,5:4},
        {1:4,3:1,4:6,6:3},
        {1:2,2:6,5:1,6:5},
        {1:5,2:1,5:6,6:2},
        {1:3,3:6,4:1,6:4},
        {2:4,3:2,4:5,5:3},
    ]
    return cube[m][u]

d=input().split()
for i in range(int(input())):
    num = input().split()

    p = d.index(num[0])
    s = int(d.index(num[1])) + 1

    print("{}".format(d[(right_num(p, s)-1)]))


