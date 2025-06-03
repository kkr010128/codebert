inp = input()
a = inp.split()
a[0] = int(a[0])
a[1] = int(a[1])
a[2] = int(a[2])
c = 0
for i in range(a[0],a[1]+1):
    if a[2] % i == 0:
        c += 1
print(c)
