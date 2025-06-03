array = []
while True:
    n = input()
    if n == "0 0":
        break
    array.append(n.split())
for i in range(len(array)):
    for i2 in range(int(array[i][0])):
        for i3 in range(int(array[i][1])):
            if i3 == int(array[i][1])-1:
                print("#")
            else:
                print("#",end="")
    print("")