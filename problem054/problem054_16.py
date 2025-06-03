z = input()
d = {}
c = 0

L = ['S','H','C','D']
for i in L:
    for j in range(1,14):
        d[i] = d.get(i,[]) + [j]


while c < z:
    x = raw_input().split()
    d[x[0]].remove(int(x[1]))
    c += 1


for i in L:
    for j in sorted(d[i]):
        print i + " " + str(j)