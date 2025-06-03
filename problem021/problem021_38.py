li1 = []
li2 = []
ans = 0
for i, s in enumerate(input()):
    if s == "\\":
        li1.append(i)
    elif s == "/" and li1:
        j = li1.pop()
        c = i - j
        ans += c
        while li2 and li2[-1][0] > j:
            c += li2[-1][1]
            li2.pop()
        li2.append((j, c))
print(ans)
if li2:
    print(len(li2), *list(zip(*li2))[1])
else:
    print(0)

