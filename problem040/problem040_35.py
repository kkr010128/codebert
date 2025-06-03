a = [i for i in input().split()]
b = []

for i in range(len(a)):
    b.append(a.pop(a.index(min(a))))

print(" ".join([str(i) for i in b]))