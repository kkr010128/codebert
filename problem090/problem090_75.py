
flag = True
count = 0
l = []

for s in input():
    if flag:
        if s == "R":
            count += 1
            l.append(count)
        else:
            l.append(0)
            count = 0


print(max(l))
