r, c = map(int, input().split())

a, btm = [], []

for i in range(r):
    a.append(list(map(int, input().split())))
    a[i].append(sum(a[i]))
    print(*a[i])

rotate = list(zip(*a))
for i in range(len(rotate)):
    btm.append(sum(rotate[i]))

print(*btm)

