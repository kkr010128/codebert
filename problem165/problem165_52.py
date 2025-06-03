from sys import stdin
data = stdin.readlines()

n = int(data[0].split()[0])

l = []
for i in range(n):
    l.append(data[i+1].split()[0])
print(len(set(l)))