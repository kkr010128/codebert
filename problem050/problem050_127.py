# coding: utf-8

list = []

while True:
    num = input().rstrip().split(" ")
    if (int(num[0]) == 0) and (int(num[1]) == 0):
        break
    list.append(num)

for i in range(len(list)):
    for j in range(int(list[i][0])):
        if (j == 0) or (j == (int(list[i][0])-1)):
            print("#"*int(list[i][1]))
        else:
            print("#" + "."*(int((list[i][1]))-2) + "#")
    print()