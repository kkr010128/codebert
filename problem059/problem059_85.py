l = input().split()
r = int(l[0])
c = int(l[1])

a = []
for i in range(r):
    a.append(list(map(int, input().split())))

for i in range(len(a)):
    a[i].insert(c, sum(a[i]))

b = []
a.append(b)

for i in range(c): #4
    s = 0
    for j in range(r): #5
        s += a[j][i]
    a[-1].append(s)
a[-1].append(sum(a[-1]))

for i in range(len(a)):
    print(*a[i])