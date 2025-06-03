a = []
try:
    while True:
        a.append(input())
except EOFError:
    pass

for i in range(len(a)):
    a[i] = a[i].lower()

b=" ".join(a)

for j in "abcdefghijklmnopqrstuvwxyz":
    print(j,":",b.count(j))
