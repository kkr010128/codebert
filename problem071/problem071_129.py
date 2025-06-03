input_n = input()
n = str(input_n)

listN = list(n)
#listN = n.split(' ')

if listN[len(listN) - 1] == "s":
    listN.append("e")
    listN.append("s")
else:
    listN.append("s")

for i in range(len(listN)):
    print(listN[i], end = "")
