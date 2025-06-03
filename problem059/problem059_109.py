data = []
da = []
a = input().split()
a[0] = int(a[0])
a[1] = int(a[1])
for i in range(a[0]):
    b = input().split()
    for j in range(a[1]):
        b[j] = int(b[j])
    data.append(b)
for i in range(len(data)):
    data[i].append(sum(data[i]))
for i in range(a[1]+1):
    da.append(0)
for i in range(a[0]):
    for j in range(a[1]+1):
        da[j] += data[i][j]
data.append(da)
for i in data:
    for j in range(len(i)):
        i[j] = str(i[j])
for i in data:
    print(" ".join(i))

