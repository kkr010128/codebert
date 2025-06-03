i = input()
i = i.split(" ")
i = list(map(int,i))

if i[0] < i[1]:
    print("a < b")
elif i[0] > i[1]:
    print("a > b")
elif i[0] == i[1]:
    print("a == b")