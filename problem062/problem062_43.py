b = []
while True:
    a = input()
    k = 0
    if a != "0":
        for i in range(len(a)):
            k += int(a[i])
        b.append(k)
    else:
        break
for i in range(len(b)):
    print(b[i])
