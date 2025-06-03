

m = []
a = 0
for i in range(input()+1):
    if i == 0:
        continue
    if i % 3 == 0:
        m.append(str(i))
    else:
        a = i
        while True:
            if a % 10 == 3:
                m.append(str(i))
                break
            a /= 10
            if a == 0:
                break
print " " + " ".join(m)