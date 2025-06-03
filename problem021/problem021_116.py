li1 = []
li2 = []
for i, s in enumerate(input()):
    if s == "\\":
        li1.append(i)
    elif s == "/" and li1:
        j = li1.pop()
        c = i - j
        while li2 and li2[-1][0] > j:
            c += li2[-1][1]
            li2.pop()
        li2.append((j, c))
if li2:
    li3 = list(zip(*li2))[1]
    print(sum(li3))
    print(len(li3), *li3)
else:
    print(0, 0, sep="\n")

