l = input().split()
a = int(l[0])
b = int(l[1])
c = int(l[2])

d = []
for i in range(a,b+1):
    if c % i == 0:
        d.append(i)
print(len(d))